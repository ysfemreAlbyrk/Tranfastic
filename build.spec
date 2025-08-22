# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from pathlib import Path

# Add src to path to import version
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from version import __version__, VERSION_INFO

print(f"Building Tranfastic v{__version__}")

a = Analysis(
    ['main.py'],
    pathex=[str(src_path)],
    binaries=[],
    datas=[
        ('assets', 'assets'),  # Include assets folder
    ],
    hiddenimports=[
        'PyQt5.QtCore',
        'PyQt5.QtWidgets', 
        'PyQt5.QtGui',
        'pystray._win32',
        'PIL._tkinter_finder',
        'googletrans',
        'keyboard',
        'pynput',
        'requests',
        'pyperclip'
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
    version='version_info.py',  # Version information
    version_file_version=VERSION_INFO,
    version_product_version=VERSION_INFO,
    version_product_name='Tranfastic',
    version_file_description='Instant Translator Application',
    version_legal_copyright='MIT License - Open Source Project',
    version_company_name='Yusuf Emre Albayrak'
) 