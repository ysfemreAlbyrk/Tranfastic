# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from pathlib import Path

# Add src to path to import version
src_path = Path(os.getcwd()) / "src"
sys.path.insert(0, str(src_path))

from version import __version__, VERSION_INFO

print(f"Building Tranfastic v{__version__}")

a = Analysis(
    ['main.py'],
    pathex=[str(src_path), str(Path(os.getcwd()) / ".venv" / "Lib" / "site-packages")],
    binaries=[
        (str(Path(os.getcwd()) / ".venv" / "Lib" / "site-packages" / "PyQt5" / "Qt5" / "bin" / "*.dll"), "PyQt5/Qt5/bin"),
    ],
    datas=[
        ('assets/icon.ico', 'assets'),
        ('assets/icon.png', 'assets'),
        ('assets/Inter', 'assets/Inter'),
        ('assets/Material_Symbols_Rounded', 'assets/Material_Symbols_Rounded'),
    ],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtWidgets', 
        'PyQt5.QtGui',
        'PyQt5.sip',
        'PyQt5.QtPrintSupport',
        'PyQt5.QtNetwork',
        'PyQt5.QtOpenGL',
        'sip',
        'pystray',
        'pystray._base',
        'pystray._win32',
        'PIL',
        'PIL.Image',
        'PIL._tkinter_finder',
        'requests',
        'keyboard',
        'pyperclip',
        'googletrans',
        'src',
        'src.app',
        'src.core',
        'src.ui',
        'src.utils',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Tranfastic',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',  # Application icon
    version='version_info.py'  # Version information
) 