"""
Tranfastic Settings Window Module
Settings configuration interface
"""

import logging
import webbrowser
from typing import Optional
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QPushButton, QLineEdit, QCheckBox, QGroupBox, QTabWidget,
    QTextEdit, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

from ..config import COLORS, APP_NAME, APP_VERSION, APP_AUTHOR, GITHUB_URL, SUPPORTED_LANGUAGES
from ..hotkey_manager import hotkey_manager

class SettingsWindow(QWidget):
    """Settings configuration window"""
    
    settings_changed = pyqtSignal()
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        self.setup_ui()
        self.load_settings()
    
    def setup_ui(self):
        """Setup user interface"""
        # Window properties
        self.setWindowTitle(f"{APP_NAME} - Settings")
        self.setFixedSize(500, 600)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {COLORS['background']};
                color: {COLORS['text']};
            }}
            QTabWidget::pane {{
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
            }}
            QTabBar::tab {{
                background-color: {COLORS['secondary']};
                color: {COLORS['text']};
                padding: 8px 16px;
                border: 1px solid {COLORS['border']};
                border-bottom: none;
                border-radius: 4px 4px 0 0;
            }}
            QTabBar::tab:selected {{
                background-color: {COLORS['accent']};
            }}
            QGroupBox {{
                font-weight: bold;
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                margin-top: 8px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 4px 0 4px;
            }}
            QComboBox, QLineEdit {{
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
        """)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Tab widget
        tab_widget = QTabWidget()
        
        # General settings tab
        general_tab = self.create_general_tab()
        tab_widget.addTab(general_tab, "General")
        
        # About tab
        about_tab = self.create_about_tab()
        tab_widget.addTab(about_tab, "About")
        
        layout.addWidget(tab_widget)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_settings)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def create_general_tab(self) -> QWidget:
        """Create general settings tab"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Language settings group
        lang_group = QGroupBox("Language Settings")
        lang_layout = QVBoxLayout()
        
        # Source language
        source_layout = QHBoxLayout()
        source_layout.addWidget(QLabel("Source Language:"))
        self.source_combo = QComboBox()
        for code, name in SUPPORTED_LANGUAGES.items():
            self.source_combo.addItem(name, code)
        source_layout.addWidget(self.source_combo)
        lang_layout.addLayout(source_layout)
        
        # Target language
        target_layout = QHBoxLayout()
        target_layout.addWidget(QLabel("Target Language:"))
        self.target_combo = QComboBox()
        for code, name in SUPPORTED_LANGUAGES.items():
            if code != "auto":  # Don't allow auto as target
                self.target_combo.addItem(name, code)
        target_layout.addWidget(self.target_combo)
        lang_layout.addLayout(target_layout)
        
        lang_group.setLayout(lang_layout)
        layout.addWidget(lang_group)
        
        # Hotkey settings group
        hotkey_group = QGroupBox("Hotkey Settings")
        hotkey_layout = QVBoxLayout()
        
        hotkey_layout.addWidget(QLabel("Global Hotkey:"))
        self.hotkey_input = QLineEdit()
        self.hotkey_input.setPlaceholderText("e.g., shift+alt+d")
        hotkey_layout.addWidget(self.hotkey_input)
        
        hotkey_layout.addWidget(QLabel("Press the key combination and it will appear here"))
        
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)
        
        # Application settings group
        app_group = QGroupBox("Application Settings")
        app_layout = QVBoxLayout()
        
        self.start_on_boot_cb = QCheckBox("Start on Windows boot")
        app_layout.addWidget(self.start_on_boot_cb)
        
        self.save_history_cb = QCheckBox("Save translation history (local)")
        app_layout.addWidget(self.save_history_cb)
        
        app_group.setLayout(app_layout)
        layout.addWidget(app_group)
        
        layout.addStretch()
        tab.setLayout(layout)
        return tab
    
    def create_about_tab(self) -> QWidget:
        """Create about tab"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # App info
        info_group = QGroupBox("Application Information")
        info_layout = QVBoxLayout()
        
        info_layout.addWidget(QLabel(f"Name: {APP_NAME}"))
        info_layout.addWidget(QLabel(f"Version: {APP_VERSION}"))
        info_layout.addWidget(QLabel(f"Author: {APP_AUTHOR}"))
        
        # GitHub link
        github_layout = QHBoxLayout()
        github_layout.addWidget(QLabel("GitHub:"))
        github_btn = QPushButton("Open Repository")
        github_btn.clicked.connect(lambda: webbrowser.open(GITHUB_URL))
        github_layout.addWidget(github_btn)
        info_layout.addLayout(github_layout)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Description
        desc_group = QGroupBox("Description")
        desc_layout = QVBoxLayout()
        
        desc_text = QTextEdit()
        desc_text.setReadOnly(True)
        desc_text.setMaximumHeight(150)
        desc_text.setPlainText(
            "Tranfastic is a lightweight Python application designed for instant, "
            "real-time translation while you work. It sits discreetly in your system tray, "
            "and a quick hotkey opens a window for text input, making translated text "
            "readily available for copying or inserting.\n\n"
            "Features:\n"
            "• Real-time translation\n"
            "• Global hotkey activation\n"
            "• System tray integration\n"
            "• Privacy focused\n"
            "• Clean, minimalist interface"
        )
        desc_layout.addWidget(desc_text)
        
        desc_group.setLayout(desc_layout)
        layout.addWidget(desc_group)
        
        # License
        license_group = QGroupBox("License")
        license_layout = QVBoxLayout()
        
        license_text = QTextEdit()
        license_text.setReadOnly(True)
        license_text.setMaximumHeight(100)
        license_text.setPlainText(
            "This project is licensed under the MIT License.\n\n"
            "MIT License - A short and simple permissive license with conditions "
            "only requiring preservation of copyright and license notices."
        )
        license_layout.addWidget(license_text)
        
        license_group.setLayout(license_layout)
        layout.addWidget(license_group)
        
        layout.addStretch()
        tab.setLayout(layout)
        return tab
    
    def load_settings(self):
        """Load current settings into UI"""
        # Language settings
        source_lang = self.config.get("source_language", "auto")
        target_lang = self.config.get("target_language", "en")
        
        source_index = self.source_combo.findData(source_lang)
        if source_index >= 0:
            self.source_combo.setCurrentIndex(source_index)
        
        target_index = self.target_combo.findData(target_lang)
        if target_index >= 0:
            self.target_combo.setCurrentIndex(target_index)
        
        # Hotkey setting
        hotkey = self.config.get("hotkey", "shift+alt+d")
        self.hotkey_input.setText(hotkey)
        
        # Application settings
        self.start_on_boot_cb.setChecked(self.config.get("start_on_boot", False))
        self.save_history_cb.setChecked(self.config.get("save_history", False))
    
    def save_settings(self):
        """Save settings from UI to config"""
        try:
            # Language settings
            source_lang = self.source_combo.currentData()
            target_lang = self.target_combo.currentData()
            
            self.config.set("source_language", source_lang)
            self.config.set("target_language", target_lang)
            
            # Hotkey setting
            hotkey = self.hotkey_input.text().strip()
            if hotkey and hotkey != self.config.get("hotkey"):
                if hotkey_manager.set_hotkey(hotkey):
                    self.config.set("hotkey", hotkey)
                else:
                    self.logger.error("Failed to set hotkey")
            
            # Application settings
            self.config.set("start_on_boot", self.start_on_boot_cb.isChecked())
            self.config.set("save_history", self.save_history_cb.isChecked())
            
            self.settings_changed.emit()
            self.close()
            
        except Exception as e:
            self.logger.error(f"Failed to save settings: {e}")
    
    def closeEvent(self, event):
        """Handle close event"""
        # Reset to original settings if not saved
        self.load_settings()
        super().closeEvent(event) 