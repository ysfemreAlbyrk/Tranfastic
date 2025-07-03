"""
Tranfastic System Tray Manager Module
Handles system tray integration and menu
"""

import logging
import subprocess
import os
from pathlib import Path
from typing import Optional, Callable
import pystray
from PIL import Image

from .config import APP_NAME, APP_VERSION

class TrayManager:
    """System tray manager for Tranfastic"""
    
    def __init__(self, on_settings: Callable, on_restart: Callable, on_exit: Callable):
        self.logger = logging.getLogger(__name__)
        self.on_settings = on_settings
        self.on_restart = on_restart
        self.on_exit = on_exit
        self.icon = None
        self._create_icon()
    
    def _create_icon(self):
        """Create system tray icon from assets/icon.png"""
        try:
            # Load icon from file
            icon_path = Path(__file__).parent.parent / "assets" / "icon.png"
            if not icon_path.exists():
                self.logger.warning(f"Icon file not found: {icon_path}, using default")
                image = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
            else:
                image = Image.open(icon_path)
            
            # Create menu
            menu = pystray.Menu(
                pystray.MenuItem("Settings", self._on_settings_click),
                pystray.MenuItem("Translation History", self._on_history_click),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem("Restart", self._on_restart_click),
                pystray.MenuItem("Exit", self._on_exit_click)
            )
            
            # Create icon
            self.icon = pystray.Icon(
                "tranfastic",
                image,
                f"{APP_NAME} v{APP_VERSION}",
                menu
            )
            
            self.logger.info("System tray icon created successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to create system tray icon: {e}")
    
    def _on_settings_click(self, icon, item):
        """Handle settings menu click"""
        try:
            self.on_settings()
        except Exception as e:
            self.logger.error(f"Settings click error: {e}")
    
    def _on_history_click(self, icon, item):
        """Handle history menu click"""
        try:
            # Open translation history folder
            history_dir = Path.home() / ".tranfastic" / "history"
            history_dir.mkdir(exist_ok=True)
            
            if os.name == 'nt':  # Windows
                subprocess.run(['explorer', str(history_dir)])
            else:  # Linux/Mac
                subprocess.run(['xdg-open', str(history_dir)])
                
        except Exception as e:
            self.logger.error(f"History click error: {e}")
    
    def _on_restart_click(self, icon, item):
        """Handle restart menu click"""
        try:
            self.on_restart()
        except Exception as e:
            self.logger.error(f"Restart click error: {e}")
    
    def _on_exit_click(self, icon, item):
        """Handle exit menu click"""
        try:
            self.on_exit()
        except Exception as e:
            self.logger.error(f"Exit click error: {e}")
    
    def show(self):
        """Show system tray icon"""
        if self.icon:
            try:
                self.icon.run()
            except Exception as e:
                self.logger.error(f"Failed to show system tray icon: {e}")
    
    def stop(self):
        """Stop system tray icon"""
        if self.icon:
            try:
                self.icon.stop()
            except Exception as e:
                self.logger.error(f"Failed to stop system tray icon: {e}")
    
    def update_tooltip(self, text: str):
        """Update icon tooltip"""
        if self.icon:
            try:
                self.icon.title = text
            except Exception as e:
                self.logger.error(f"Failed to update tooltip: {e}")
    
    def show_notification(self, title: str, message: str):
        """Show system notification"""
        if self.icon:
            try:
                self.icon.notify(title, message)
            except Exception as e:
                self.logger.error(f"Failed to show notification: {e}") 