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

from src.utils.config import Config, APP_ICON_PATH, APP_TEXT_FONT_PATH, APP_SYMBOL_FONT_PATH
from src.utils.logger import setup_logging, cleanup_old_logs
from src.core.translator import translator_engine
from src.core.hotkey_manager import hotkey_manager
from src.core.tray_manager import TrayManager
from src.core.clipboard_manager import clipboard_manager
from src.ui.translation_window import TranslationWindow
from src.ui.settings_window import SettingsWindow
from src.core.updater import AutoUpdater, check_for_updates_startup
from src.utils.runtime import should_enable_auto_update

def load_custom_fonts(app):
    """Load custom fonts for the application"""
    inter_font_path = str((Path(__file__).parent.parent / APP_TEXT_FONT_PATH).resolve())
    QFontDatabase.addApplicationFont(inter_font_path)
    material_font_path = str((Path(__file__).parent.parent / APP_SYMBOL_FONT_PATH).resolve())
    QFontDatabase.addApplicationFont(material_font_path)
    app.setFont(QFont("Inter"))

class TrayThread(QThread):
    """Thread for running system tray"""
    settings_requested = pyqtSignal()
    restart_requested = pyqtSignal()
    exit_requested = pyqtSignal()
    check_updates_requested = pyqtSignal()
    
    def __init__(self, on_settings, on_restart, on_exit, on_check_updates=None):
        super().__init__()
        self.on_settings = on_settings
        self.on_restart = on_restart
        self.on_exit = on_exit
        self.on_check_updates = on_check_updates
        self.tray_manager = None
    
    def run(self):
        """Run tray manager in separate thread"""
        self.tray_manager = TrayManager(
            on_settings=lambda: self.settings_requested.emit(),
            on_restart=lambda: self.restart_requested.emit(),
            on_exit=lambda: self.exit_requested.emit(),
            on_check_updates=lambda: self.check_updates_requested.emit() if self.on_check_updates else None
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
        icon_path = str((Path(__file__).parent.parent / APP_ICON_PATH).resolve())
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
        self.auto_updater = None
        
        # Setup application
        self.setup_application()
        
    def setup_application(self):
        """Setup application components"""
        try:
            self.logger.info("Starting application setup...")
            self.logger.info(f"Working directory: {os.getcwd()}")
            self.logger.info(f"Executable path: {sys.executable}")
            self.logger.info(f"Script path: {sys.argv[0]}")
            
            # Setup hotkey manager
            self.logger.info("Setting up hotkey manager...")
            hotkey_manager.set_callback(self.show_translation_window)
            hotkey_manager.set_hotkey(self.config.get("hotkey", "shift+alt+d"))
            
            # Setup tray manager in separate thread
            update_callback = self.check_for_updates_manual if should_enable_auto_update() else None
            self.tray_thread = TrayThread(
                on_settings=self.show_settings_window,
                on_restart=self.restart_application,
                on_exit=self.quit_application,
                on_check_updates=update_callback
            )
            self.tray_thread.settings_requested.connect(self.show_settings_window)
            self.tray_thread.restart_requested.connect(self.restart_application)
            self.tray_thread.exit_requested.connect(self.quit_application)
            if should_enable_auto_update():
                self.tray_thread.check_updates_requested.connect(self.check_for_updates_manual)
            self.tray_thread.start()
            
            # Setup clipboard manager
            clipboard_manager.app = self.app
            
            # Setup auto-updater (only for installed versions)
            if should_enable_auto_update():
                self.logger.info("Setting up auto-updater...")
                self.auto_updater = AutoUpdater(parent_widget=None)
                
                # Schedule periodic update checks (every 24 hours)
                self.update_timer = self.auto_updater.schedule_periodic_check(24)
                
                # Check for updates at startup (after 5 seconds delay)
                QTimer.singleShot(5000, lambda: self.auto_updater.check_for_updates(silent=True))
            else:
                self.logger.info("Auto-updater disabled (portable version)")
                self.auto_updater = None
            
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
            
            from src.utils.logger import log_translation
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
            
            # Update translation window size if changed
            if self.translation_window and self.translation_window.isVisible():
                self.translation_window.set_window_size()
                self.translation_window.center_window()
            
            # Startup setting is automatically handled by Config class
            
            self.logger.info(f"Settings updated, config: \n{self.config.config}")
            
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

    def check_for_updates_manual(self):
        """Manually check for updates (triggered from tray menu)"""
        try:
            if self.auto_updater and should_enable_auto_update():
                self.auto_updater.check_for_updates(silent=False)
            else:
                self.logger.info("Update check skipped (portable version)")
        except Exception as e:
            self.logger.error(f"Manual update check failed: {e}")

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
