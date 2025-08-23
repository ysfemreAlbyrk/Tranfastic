"""
General Settings Tab Module
Contains language, hotkey and application settings
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QPushButton, QLineEdit, QCheckBox, QGroupBox, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from ...utils.config import COLORS, SUPPORTED_LANGUAGES


class GeneralTab(QWidget):
    """General settings tab widget"""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.setup_ui()
    
    def setup_ui(self):
        """Setup general tab UI"""
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        layout.setSpacing(12)

        # Language settings group
        lang_group = QGroupBox("Language Settings")
        lang_layout = QVBoxLayout()
        lang_layout.setSpacing(12)
        
        # Top row: Language titles
        titles_layout = QHBoxLayout()
        titles_layout.setSpacing(20)
        
        source_label = QLabel("Source Language")
        source_label.setAlignment(Qt.AlignCenter)
        titles_layout.addWidget(source_label, stretch=1)
        
        # Fixed width spacer for arrow area
        spacer = QLabel()
        spacer.setFixedWidth(40)  # Match arrow label width
        titles_layout.addWidget(spacer)
        
        target_label = QLabel("Target Language")
        target_label.setAlignment(Qt.AlignCenter)
        titles_layout.addWidget(target_label, stretch=1)
        
        lang_layout.addLayout(titles_layout)

        # Bottom line
        hr = QFrame()
        hr.setFrameShape(QFrame.HLine)
        hr.setFrameShadow(QFrame.Sunken)
        hr.setFixedHeight(1)
        hr.setStyleSheet(f"background-color: {COLORS['border']}; color: {COLORS['border']}; height: 1px;")
        lang_layout.addWidget(hr)
        
        # Bottom row: Dropdowns and arrow
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(20)
        
        # Source dropdown
        self.source_combo = QComboBox()
        for code, name in SUPPORTED_LANGUAGES.items():
            self.source_combo.addItem(name, code)
        controls_layout.addWidget(self.source_combo, stretch=1)
        
        # Arrow
        arrow_label = QLabel('\uf108\ue5df ')
        arrow_label.setStyleSheet("font-size: 24px; color: #888; font-weight: bold;letter-spacing: -15px;")
        arrow_label.setFont(QFont("Material Symbols Rounded"))
        arrow_label.setAlignment(Qt.AlignCenter)
        arrow_label.setFixedWidth(40)
        controls_layout.addWidget(arrow_label, stretch=0)
        
        # Target dropdown
        self.target_combo = QComboBox()
        for code, name in SUPPORTED_LANGUAGES.items():
            if code != "auto":
                self.target_combo.addItem(name, code)
        controls_layout.addWidget(self.target_combo, stretch=1)
        
        lang_layout.addLayout(controls_layout)

        # Info area
        info_layout = QHBoxLayout()
        info_layout.setSpacing(6)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_icon = QLabel("info")
        info_icon.setStyleSheet("color: #888; font-size: 16px;")
        info_icon.setFont(QFont("Material Symbols Rounded"))
        info_layout.addWidget(info_icon)
        info_text = QLabel("Please avoid using 'Auto Detect' for faster and more accurate translation.")
        info_text.setStyleSheet("color: #888; font-style: italic;")
        info_text.setWordWrap(True)
        info_layout.addWidget(info_text, stretch=1)
        lang_layout.addLayout(info_layout)
        lang_group.setLayout(lang_layout)
        layout.addWidget(lang_group)

        # Hotkey settings group
        hotkey_group = QGroupBox("Hotkey Settings")
        hotkey_layout = QVBoxLayout()
        hotkey_layout.setSpacing(6)
        hotkey_layout.addWidget(QLabel("Global Hotkey:"))
        self.hotkey_input = QLineEdit()
        self.hotkey_input.setPlaceholderText("e.g., shift+alt+d")
        hotkey_layout.addWidget(self.hotkey_input)
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)

        # Application settings group
        app_group = QGroupBox("Application Settings")
        app_layout = QVBoxLayout()
        app_layout.setSpacing(6)
        self.start_on_boot_cb = QCheckBox("Start on Windows boot")
        app_layout.addWidget(self.start_on_boot_cb)
        self.save_history_cb = QCheckBox("Save translation history (local)")
        app_layout.addWidget(self.save_history_cb)
        self.restore_clipboard_cb = QCheckBox("Restore original clipboard after translation")
        app_layout.addWidget(self.restore_clipboard_cb)
        
        app_group.setLayout(app_layout)
        layout.addWidget(app_group)

        layout.addStretch()
        self.setLayout(layout)
    
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
        self.restore_clipboard_cb.setChecked(self.config.get("restore_clipboard", False))
    
    def get_settings(self):
        """Get current settings from UI"""
        return {
            "source_language": self.source_combo.currentData(),
            "target_language": self.target_combo.currentData(),
            "hotkey": self.hotkey_input.text().strip(),
            "start_on_boot": self.start_on_boot_cb.isChecked(),
            "save_history": self.save_history_cb.isChecked(),
            "restore_clipboard": self.restore_clipboard_cb.isChecked()
        }
