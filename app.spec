# -*- mode: python ; coding: utf-8 -*-

# WARNING: The `.env` bundled below MUST be a separate production artifact
# (for example `build/.env.prod` or `.env.prod` copied to `.env` only at
# build time). Never bundle the development `.env` from the repository into
# the distributed binary, and never commit a `.env` that contains real
# production secrets. See the "Production" section of README.md for details.

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
