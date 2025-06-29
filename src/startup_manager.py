"""
Tranfastic Startup Manager
Manages Windows startup functionality
"""

import os
import sys
import logging
from pathlib import Path
from typing import Optional

# Import winreg only on Windows
try:
    import winreg
    WINDOWS_AVAILABLE = True
except ImportError:
    WINDOWS_AVAILABLE = False

class StartupManager:
    """Manages application startup on Windows boot"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.app_name = "Tranfastic"
        
        if WINDOWS_AVAILABLE:
            self.registry_key = winreg.HKEY_CURRENT_USER
            self.registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        else:
            self.registry_key = None
            self.registry_path = None
        
    def get_executable_path(self) -> str:
        """Get the path to the main executable"""
        if getattr(sys, 'frozen', False):
            # Running as PyInstaller bundle
            return sys.executable
        else:
            # Running as Python script
            main_py_path = Path(__file__).parent.parent / "main.py"
            python_exe = sys.executable
            return f'"{python_exe}" "{main_py_path}"'
    
    def is_startup_enabled(self) -> bool:
        """Check if application is set to start on boot"""
        if not WINDOWS_AVAILABLE:
            return False
            
        try:
            with winreg.OpenKey(self.registry_key, self.registry_path) as key:
                try:
                    value, _ = winreg.QueryValueEx(key, self.app_name)
                    return True
                except FileNotFoundError:
                    return False
        except Exception as e:
            self.logger.error(f"Failed to check startup status: {e}")
            return False
    
    def enable_startup(self) -> bool:
        """Enable application startup on Windows boot"""
        if not WINDOWS_AVAILABLE:
            self.logger.warning("Windows registry not available - startup setting ignored")
            return False
            
        try:
            executable_path = self.get_executable_path()
            
            with winreg.OpenKey(self.registry_key, self.registry_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, self.app_name, 0, winreg.REG_SZ, executable_path)
            
            self.logger.info(f"Startup enabled: {executable_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to enable startup: {e}")
            return False
    
    def disable_startup(self) -> bool:
        """Disable application startup on Windows boot"""
        if not WINDOWS_AVAILABLE:
            self.logger.warning("Windows registry not available - startup setting ignored")
            return False
            
        try:
            with winreg.OpenKey(self.registry_key, self.registry_path, 0, winreg.KEY_SET_VALUE) as key:
                try:
                    winreg.DeleteValue(key, self.app_name)
                    self.logger.info("Startup disabled")
                    return True
                except FileNotFoundError:
                    # Already not in startup - this is fine
                    return True
                    
        except Exception as e:
            self.logger.error(f"Failed to disable startup: {e}")
            return False
    
    def set_startup(self, enabled: bool) -> bool:
        """Set startup status"""
        if enabled:
            return self.enable_startup()
        else:
            return self.disable_startup()

# Global instance
startup_manager = StartupManager() 