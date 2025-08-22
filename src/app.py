#!/usr/bin/env python3
"""
Tranfastic - Instant Translator Application
Main application class and logic
"""

import sys
import os
from pathlib import Path

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QFontDatabase, QFont, QIcon

from .utils.config import Config
from .utils.logger import setup_logging, cleanup_old_logs
from .core.translator import translator_engine
from .core.hotkey_manager import hotkey_manager
from .core.tray_manager import TrayManager
from .core.clipboard_manager import clipboard_manager
from .ui.translation_window import TranslationWindow
from .ui.settings_window import SettingsWindow

def load_custom_fonts(app):
    """Load custom fonts for the application"""
    inter_font_path = str((Path(__file__).parent.parent / "assets/Inter/Inter-VariableFont_opsz,wght.ttf").resolve())
    QFontDatabase.addApplicationFont(inter_font_path)
    material_font_path = str((Path(__file__).parent.parent / "assets/Material_Symbols_Rounded/MaterialSymbolsRounded-VariableFont_FILL,GRAD,opsz,wght.ttf").resolve())
    QFontDatabase.addApplicationFont(material_font_path)
    app.setFont(QFont("Inter"))

class TrayThread(QThread):
    """Thread for running system tray"""
    settings_requested = pyqtSignal()
    restart_requested = pyqtSignal()
    exit_requested = pyqtSignal()
    
    def __init__(self, on_settings, on_restart, on_exit):
        super().__init__()
        self.on_settings = on_settings
        self.on_restart = on_restart
        self.on_exit = on_exit
        self.tray_manager = None
    
    def run(self):
        """Run tray manager in separate thread"""
        self.tray_manager = TrayManager(
            on_settings=lambda: self.settings_requested.emit(),
            on_restart=lambda: self.restart_requested.emit(),
            on_exit=lambda: self.exit_requested.emit()
        )
        self.tray_manager.show()
    
    def stop(self):
        """Stop tray manager"""
        if self.tray_manager:
            self.tray_manager.stop()

class TranfasticApp:
    """Main application class"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        load_custom_fonts(self.app)
        self.app.setQuitOnLastWindowClosed(False)  # Keep running when windows are closed
        
        # Set application icon
        icon_path = str((Path(__file__).parent.parent / "assets/icon.png").resolve())
        self.app.setWindowIcon(QIcon(icon_path))
        
        # Setup logging
        self.logger = setup_logging()
        
        # Cleanup old logs
        cleanup_old_logs()
        
        # Initialize components
        self.config = Config()
        self.tray_thread = None
        self.translation_window = None
        self.settings_window = None
        
        # Setup application
        self.setup_application()
        
    def setup_application(self):
        """Setup application components"""
        try:
            # Setup hotkey manager
            hotkey_manager.set_callback(self.show_translation_window)
            hotkey_manager.set_hotkey(self.config.get("hotkey", "shift+alt+d"))
            
            # Setup tray manager in separate thread
            self.tray_thread = TrayThread(
                on_settings=self.show_settings_window,
                on_restart=self.restart_application,
                on_exit=self.quit_application
            )
            self.tray_thread.settings_requested.connect(self.show_settings_window)
            self.tray_thread.restart_requested.connect(self.restart_application)
            self.tray_thread.exit_requested.connect(self.quit_application)
            self.tray_thread.start()
            
            # Setup clipboard manager
            clipboard_manager.app = self.app
            
            # Log successful setup
            self.logger.info("Application setup completed successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to setup application: {e}")
            sys.exit(1)
    
    def show_translation_window(self):
        """Show translation window"""
        try:
            if self.translation_window is None or not self.translation_window.isVisible():
                self.translation_window = TranslationWindow(
                    config=self.config,
                    on_translation_complete=self.handle_translation_complete
                )
                self.translation_window.show()
                self.translation_window.raise_()
                self.translation_window.activateWindow()
                
                self.logger.info("Translation window opened")
            else:
                # Bring existing window to front
                self.translation_window.raise_()
                self.translation_window.activateWindow()
                
        except Exception as e:
            self.logger.error(f"Failed to show translation window: {e}")
    
    def show_settings_window(self):
        """Show settings window"""
        try:
            if self.settings_window is None or not self.settings_window.isVisible():
                self.settings_window = SettingsWindow(config=self.config)
                self.settings_window.settings_changed.connect(self.on_settings_changed)
                self.settings_window.show()
                self.settings_window.raise_()
                self.settings_window.activateWindow()
                
                self.logger.info("Settings window opened")
            else:
                # Bring existing window to front
                self.settings_window.raise_()
                self.settings_window.activateWindow()
                
        except Exception as e:
            self.logger.error(f"Failed to show settings window: {e}")
    
    def handle_translation_complete(self, translated_text: str):
        """Handle translation completion"""
        try:
            # Paste translated text with config
            clipboard_manager.paste_translation(translated_text, config=self.config)
            
            # Log translation
            source_lang = self.config.get("source_language", "auto")
            target_lang = self.config.get("target_language", "en")
            
            from .utils.logger import log_translation
            log_translation("", translated_text, source_lang, target_lang, True)
            
            # Show notification
            if self.tray_thread and self.tray_thread.tray_manager:
                self.tray_thread.tray_manager.show_notification(
                    "Translation Complete",
                    f"Translated text has been pasted"
                )
                
        except Exception as e:
            self.logger.error(f"Failed to handle translation completion: {e}")
    
    def on_settings_changed(self):
        """Handle settings changes"""
        try:
            # Update hotkey if changed
            new_hotkey = self.config.get("hotkey")
            if new_hotkey != hotkey_manager.current_hotkey:
                hotkey_manager.set_hotkey(new_hotkey)
            
            # Startup setting is automatically handled by Config class
            
            self.logger.info("Settings updated")
            
        except Exception as e:
            self.logger.error(f"Failed to apply settings changes: {e}")
    
    def run(self):
        """Run the application"""
        try:
            self.logger.info("Starting Tranfastic application")
            
            # Run application event loop
            return self.app.exec_()
            
        except Exception as e:
            self.logger.error(f"Application run error: {e}")
            return 1
    
    def quit_application(self):
        """Quit the application"""
        try:
            self.logger.info("Shutting down Tranfastic application")
            
            # Cleanup components
            if hotkey_manager:
                hotkey_manager.cleanup()
            
            if self.tray_thread:
                self.tray_thread.stop()
                self.tray_thread.quit()
                self.tray_thread.wait()
            
            if clipboard_manager:
                clipboard_manager.clear_restore_timer()
            
            # Quit application
            self.app.quit()
            
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")
            sys.exit(1)

    def restart_application(self):
        """Restart the application"""
        try:
            self.logger.info("Restarting Tranfastic application")
            
            # Import subprocess for restart
            import subprocess
            
            # Get current executable and arguments
            executable = sys.executable
            script_path = sys.argv[0]
            
            # Show notification before restart
            if self.tray_thread and self.tray_thread.tray_manager:
                self.tray_thread.tray_manager.show_notification(
                    "Restarting Application",
                    "Tranfastic is restarting..."
                )
            
            # Start new process
            subprocess.Popen([executable, script_path])
            
            # Quit current application
            self.quit_application()
            
        except Exception as e:
            self.logger.error(f"Failed to restart application: {e}")
            # If restart fails, show notification and continue running
            if self.tray_thread and self.tray_thread.tray_manager:
                self.tray_thread.tray_manager.show_notification(
                    "Restart Failed",
                    "Could not restart application. Please restart manually."
                )
