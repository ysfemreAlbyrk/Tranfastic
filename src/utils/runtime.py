#!/usr/bin/env python3
"""
Runtime detection utilities
Detects if application is running as portable or installed version
"""

import os
import sys
from pathlib import Path


def is_portable() -> bool:
    """
    Detect if application is running as portable version
    
    Returns:
        bool: True if portable, False if installed
    """
    try:
        # Check if running from PyInstaller bundle
        if getattr(sys, 'frozen', False):
            exe_path = Path(sys.executable)
            
            # Portable version indicators:
            # 1. Not in Program Files
            # 2. In a "portable" directory
            # 3. Not registered in registry (we'll assume based on path)
            
            exe_dir = exe_path.parent
            exe_name = exe_path.name.lower()
            
            # Check if in Program Files (installed version)
            program_files = [
                Path(os.environ.get('PROGRAMFILES', 'C:\\Program Files')),
                Path(os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files (x86)')),
            ]
            
            for pf in program_files:
                try:
                    if pf in exe_path.parents:
                        return False  # Installed version
                except (OSError, ValueError):
                    continue
            
            # Check if in portable directory
            if 'portable' in str(exe_dir).lower():
                return True
                
            # Check if executable is in root of a directory (portable pattern)
            # vs being in a structured installation
            parent_name = exe_dir.name.lower()
            if parent_name in ['tranfastic', 'bin', 'app']:
                return False  # Likely installed
                
            return True  # Default to portable for other locations
            
        else:
            # Running from source - treat as portable for development
            return True
            
    except Exception:
        # If detection fails, default to portable (safer)
        return True


def get_version_info() -> dict:
    """
    Get version information with runtime context
    
    Returns:
        dict: Version info with runtime type
    """
    from ..version import get_version_info as base_version_info
    
    info = base_version_info()
    info['runtime_type'] = 'Portable' if is_portable() else 'Installed'
    info['is_portable'] = is_portable()
    
    return info


def get_display_version() -> str:
    """
    Get display version string with runtime context
    """
    from ..version import __version__
    
    if is_portable():
        return f"{__version__} (Portable)"
    else:
        return __version__


def should_enable_auto_update() -> bool:
    """
    Check if auto-update should be enabled
    
    Returns:
        bool: True if auto-update should be enabled
    """
    # Only enable auto-update for installed versions
    return not is_portable()
