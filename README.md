# Body Mark

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Body Mark** is a desktop application built with Python and Tkinter that calculates the **Body Mass Index (BMI)** of a person based on their weight and height. The application provides an instant health classification alongside the numeric BMI result, telling the user whether they fall into the underweight, normal weight, overweight, or obese range according to standard WHO guidelines.

The interface is intentionally simple: the user enters their weight (in kilograms) and height (in centimeters), hits the calculate button, and the result is displayed immediately — no accounts, no internet connection, no setup beyond running the script.

Under the hood, the project follows a layered architecture (config, UI, utils, constants) that keeps business logic completely separated from the interface. It also ships with a full test suite (unit + integration), environment-based configuration via `.env`, a global error handling system that surfaces validation errors as friendly dialog boxes, and a PyInstaller build pipeline that packages the app into a single standalone executable for distribution on Windows, Linux, and Mac.

The project serves as a practical reference for structuring real-world Python desktop applications with good engineering practices: clean separation of concerns, pre-commit hooks for linting and formatting, dependency security auditing with `pip-audit`, and CI-ready test configuration with `pytest`.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

All dependencies are declared in `pyproject.toml`. The `requirements*.txt` files are thin wrappers (`-e .[extra]`) kept for backward-compatible muscle memory.

#### Runtime (`[project.dependencies]`)

```
python-dotenv==1.2.2
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
mypy==1.13.0
python-semantic-release==9.21.0
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`[project.optional-dependencies]` build)

```
pyinstaller==6.16.0
```

## Getting Started

With the dependencies above in mind, follow these steps to run the app locally:

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Install the runtime, dev, and test dependencies in one shot: `pip install -e ".[dev,test]"`
6. Copy the development environment template: `cp .env.example.dev .env` (Windows: `copy .env.example.dev .env`)
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The `.env` file you copied in the previous step controls how the app boots. The template lives in `.env.example.dev`.

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e ".[test]"`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Before shipping, scan dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e ".[dev]"`
4. Execute: `pip-audit`

## Build

Once tests pass and dependencies are clean, generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Production secrets warning

> **IMPORTANT:** The `app.spec` file bundles `.env` into the distributed binary. Before building a production artifact, set your production values directly in `.env`. Never commit a `.env` containing real production secrets to the repository.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Continuous Integration

The repository ships with a **GitHub Actions** pipeline defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs automatically on every `push` and `pull_request` targeting the `main` branch. On `push` to `main`, the same workflow continues with three additional jobs that produce an automated release.

### Pipeline overview

```
                      ┌─── PR or push to main ───┐
                      ▼                          ▼
┌──────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   lint-and-audit     │─▶│       test       │─▶│      build       │
│ ruff · mypy · audit  │  │ pytest (headless)│  │ pyinstaller (lnx)│
└──────────────────────┘  └──────────────────┘  └──────────────────┘
                                                          │
                                       (only on push to main, sequentially)
                                                          ▼
                                                ┌──────────────────────┐
                                                │   prepare-release    │
                                                │ bump · changelog · tag│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │  build-windows-exe   │
                                                │ pyinstaller (windows)│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │   publish-release    │
                                                │ GitHub Release + .exe│
                                                └──────────────────────┘
```

### Validation jobs (run on every PR and push)

1. **`lint-and-audit`** — `ruff check`, `ruff format --check`, `mypy`, `pip-audit --skip-editable`.
2. **`test`** — installs Tkinter + `xvfb` on Ubuntu and runs `pytest --tb=short` headlessly.
3. **`build`** — smoke test that `pyinstaller app.spec` produces a binary on Linux.

### Release jobs (only on push to `main`)

4. **`prepare-release`** — runs [`python-semantic-release`](https://python-semantic-release.readthedocs.io/) to inspect the commits since the latest tag, decide the next SemVer version using [Conventional Commits](#conventional-commits-required-for-releases), regenerate `CHANGELOG.md`, bump `pyproject.toml`, then commit, tag and push back to `main`. The bot's release commit is `chore(release): vX.Y.Z [skip release]`, so the next workflow run is short-circuited automatically and no release loop occurs.
5. **`build-windows-exe`** — checks out the freshly created tag on a `windows-latest` runner, runs `pyinstaller app.spec`, and renames the artifact to `body-mark-vX.Y.Z-windows.exe`.
6. **`publish-release`** — uses `python-semantic-release/publish-action` to create the GitHub Release for the new tag and attaches the Windows `.exe`.

### Conventional Commits (required for releases)

Commits merged into `main` must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so the pipeline can compute the next version and group the changelog entries.

| Commit prefix | Version bump | Example |
|---|---|---|
| `feat:` / `feat(scope):` | **MINOR** | `feat(ui): add dark mode toggle` |
| `fix:` / `fix(scope):`, `perf:` / `perf(scope):` | **PATCH** | `fix: prevent crash on empty username` |
| `refactor:`, `docs:`, `build:`, `ci:`, `chore:`, `style:`, `test:` | *no release* | `refactor: extract auth helper` |
| `feat!:` / `fix!:` or `BREAKING CHANGE:` in the body | **MAJOR** | `feat!: rewrite auth API` |

When a push contains multiple commits, the highest applicable bump wins (a single `feat:` among many `fix:` triggers a MINOR bump). Commits whose prefix is not in `feat` / `fix` / `perf` (or marked as breaking) do not trigger a release on their own — they will only ship the next time a release-worthy commit lands. If you squash-merge PRs, configure the repo to use the PR title as the squash commit message and write the **PR title** following the convention.

### Skipping a release

If you need to push a change to `main` without producing a release (e.g. tweaking job names in the workflow, fixing a typo in the README), append `[skip release]` to the commit message. The validation jobs (lint, test, build) still run; only `prepare-release`, `build-windows-exe` and `publish-release` are skipped.

```bash
git commit -m "ci: rename build job for clarity [skip release]"
```

To skip **everything** including validation, use GitHub's standard `[skip ci]` marker instead.

### Where the build outputs live

| Output | Location |
|---|---|
| Validation logs (lint, tests) | **Actions** tab on GitHub |
| Linux smoke-build binary | Ephemeral, inside the runner |
| Windows `.exe` per version | **Releases** page (sidebar of the repo) |
| Version history & notes | [`CHANGELOG.md`](CHANGELOG.md) + Releases page |

> **Note:** GitHub's **Packages** section is for package registries (npm, PyPI, Docker, etc.) and does not host PyInstaller executables. Standalone binaries always live under **Releases**.

### Repository setup required for releases

For the release jobs to push tags and commits back to `main`, the repository needs:

1. **Settings → Actions → General → Workflow permissions**: set to *Read and write permissions*.
2. **Branch protection on `main`**: if enabled, allow the `github-actions[bot]` to bypass the PR requirement, or disable the protection for the bot. Otherwise `prepare-release` will fail when pushing the version bump.

### Running the same checks locally

```bash
# lint-and-audit
ruff check .
ruff format --check .
mypy --config-file=pyproject.toml .
pip-audit --skip-editable

# test
pytest --tb=short

# build
pyinstaller app.spec
```

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/body-mark`](https://www.diegolibonati.com.ar/#/project/body-mark)
