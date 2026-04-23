# Body Mark

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

**Body Mark** is a desktop application built with Python and Tkinter that calculates the **Body Mass Index (BMI)** of a person based on their weight and height. The application provides an instant health classification alongside the numeric BMI result, telling the user whether they fall into the underweight, normal weight, overweight, or obese range according to standard WHO guidelines.

The interface is intentionally simple: the user enters their weight (in kilograms) and height (in centimeters or meters), hits the calculate button, and the result is displayed immediately — no accounts, no internet connection, no setup beyond running the script.

Under the hood, the project follows a layered architecture (config, UI, utils, constants) that keeps business logic completely separated from the interface. It also ships with a full test suite (unit + integration), environment-based configuration via `.env`, a global error handling system that surfaces validation errors as friendly dialog boxes, and a PyInstaller build pipeline that packages the app into a single standalone executable for distribution on Windows, Linux, and Mac.

The project serves as a practical reference for structuring real-world Python desktop applications with good engineering practices: clean separation of concerns, pre-commit hooks for linting and formatting, dependency security auditing with `pip-audit`, and CI-ready test configuration with `pytest`.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

#### Requirements.txt

```
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/body-mark`](https://www.diegolibonati.com.ar/#/project/body-mark)

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Known Issues

None at the moment.