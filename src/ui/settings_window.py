"""
Tranfastic Settings Window Module
Main settings window that manages different setting tabs
"""

import logging
from pathlib import Path

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QMessageBox
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

from ..utils.config import COLORS, APP_NAME, APP_ICON_PATH
from ..core.hotkey_manager import hotkey_manager
from .settings_tabs import GeneralTab, AppearanceTab, AboutTab


class SettingsWindow(QWidget):
    """Main settings configuration window"""
    
    settings_changed = pyqtSignal()
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Set window icon
        icon_path = str((Path(__file__).parent.parent.parent / APP_ICON_PATH).resolve())
        self.setWindowIcon(QIcon(icon_path))
        
        self.setup_ui()
        self.load_settings()
    
    def setup_ui(self):
        """Setup user interface"""
        # Window properties
        self.setWindowTitle(f"{APP_NAME} - Settings")
        self.setFixedSize(500, 600)
        self.setStyleSheet(self._get_stylesheet())
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(12, 0, 12, 0)
        layout.setSpacing(12)
        
        # Tab widget
        tab_widget = QTabWidget()
        
        # Create tabs
        self.general_tab = GeneralTab(self.config)
        self.appearance_tab = AppearanceTab(self.config)
        self.about_tab = AboutTab()
        
        # Add tabs to widget
        tab_widget.addTab(self.general_tab, "General")
        tab_widget.addTab(self.appearance_tab, "Appearance")
        tab_widget.addTab(self.about_tab, "About")
        
        layout.addWidget(tab_widget)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 12, 12)
        button_layout.addStretch()
        
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_settings)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        cancel_btn.setStyleSheet("background-color: #444;")
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def _get_stylesheet(self):
        """Get the complete stylesheet for the window"""
        return f"""
            QWidget {{
                background-color: {COLORS['background']};
                color: {COLORS['text']};
            }}
            QTabWidget::pane {{
                border-top: 1px solid {COLORS['border']};
                border-bottom: 1px solid {COLORS['border']};
            }}
            QTabBar::tab {{
                background-color: {COLORS['background']};
                color: {COLORS['text']};
                padding: 8px 16px;
                border:none;
            }}
            QTabBar::tab:selected {{
                background-color: {COLORS['background']};
                border-bottom: 2px solid {COLORS['accent']};
            }}
            QGroupBox {{
                font-weight: bold;
                border:none;
                padding-top: 20px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
            }}
            QComboBox {{
                background-color: {COLORS['secondary']};
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                padding:6px;
                font-size: 12px;
                color: {COLORS['text']};
                min-height: 16px;
            }}
            QComboBox:hover {{
                border: 1px solid {COLORS['border']};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            QLineEdit {{
                background-color: {COLORS['secondary']};
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                padding: 6px;
                font-size: 12px;
            }}
            QPushButton {{
                background-color: {COLORS['accent']};
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-size: 12px;
            }}
            QPushButton:hover {{
                background-color: #5BA0F2;
            }}
            QCheckBox {{
                font-size: 12px;
            }}
            QLabel {{
                font-size: 12px;
            }}
        """
    
    def load_settings(self):
        """Load current settings into all tabs"""
        self.general_tab.load_settings()
        self.appearance_tab.load_settings()
    
    def save_settings(self):
        """Save settings from all tabs to config"""
        try:
            # Get settings from all tabs
            general_settings = self.general_tab.get_settings()
            appearance_settings = self.appearance_tab.get_settings()
            
            # Handle hotkey setting with validation
            current_hotkey = self.config.get("hotkey")
            new_hotkey = general_settings["hotkey"]
            
            if new_hotkey and new_hotkey != current_hotkey:
                if hotkey_manager.set_hotkey(new_hotkey):
                    self.config.set("hotkey", new_hotkey)
                else:
                    self.logger.error("Failed to set hotkey")
            
            # Handle startup setting with error handling
            try:
                current_startup = self.config.get("start_on_boot", False)
                new_startup = general_settings["start_on_boot"]
                
                if current_startup != new_startup:
                    self.config.set("start_on_boot", new_startup)
                    
            except Exception as startup_error:
                self.logger.error(f"Failed to update startup setting: {startup_error}")
                QMessageBox.warning(
                    self, 
                    "Startup Setting Error",
                    f"Failed to update Windows startup setting:\\n{str(startup_error)}\\n\\nOther settings have been saved successfully."
                )
                # Don't prevent other settings from being saved
            
            # Save all other settings
            for key, value in general_settings.items():
                if key != "hotkey":  # Already handled above
                    self.config.set(key, value)
            
            for key, value in appearance_settings.items():
                self.config.set(key, value)
            
            # Remove legacy config key if it exists
            if "monitor_behavior" in self.config.config:
                del self.config.config["monitor_behavior"]
                self.config.save_config()
            
            self.settings_changed.emit()
            self.close()
            
        except Exception as e:
            self.logger.error(f"Failed to save settings: {e}")
            QMessageBox.critical(
                self, 
                "Settings Error",
                f"Failed to save settings:\\n{str(e)}"
            )
    
    def closeEvent(self, event):
        """Handle close event"""
        # Reload settings if not saved
        self.load_settings()
        super().closeEvent(event)