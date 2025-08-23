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
    QTextEdit, QScrollArea, QFrame, QGridLayout, QRadioButton, QButtonGroup, QGraphicsDropShadowEffect,
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor
from pathlib import Path

from ..utils.config import COLORS, APP_NAME, APP_VERSION, APP_AUTHOR, GITHUB_URL, SUPPORTED_LANGUAGES, APP_ICON_PATH
from ..core.hotkey_manager import hotkey_manager

class SettingsWindow(QWidget):
    """Settings configuration window"""
    
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
        self.setStyleSheet(f"""
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
        """)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(12,0,12,0)
        layout.setSpacing(12)
        
        # Tab widget
        tab_widget = QTabWidget()
        
        # General settings tab
        general_tab = self.create_general_tab()
        tab_widget.addTab(general_tab, "General")
        
        # Popup settings tab
        popup_tab = self.create_popup_tab()
        tab_widget.addTab(popup_tab, "PopUp Window")

        # About tab
        about_tab = self.create_about_tab()
        tab_widget.addTab(about_tab, "About")
        
        layout.addWidget(tab_widget)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0,0,12,12)
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
    
    def create_general_tab(self) -> QWidget:
        """Create general settings tab"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,10,0,0)
        layout.setSpacing(12)

        # Language settings group
        lang_group = QGroupBox("Language Settings")
        lang_layout = QVBoxLayout()
        lang_layout.setSpacing(12)
        
        # Top row: Language titles
        titles_layout = QHBoxLayout()
        titles_layout.setSpacing(20)  # Remove spacing since we want labels to fill width
        
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

        # bottom line
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
        arrow_label.setStyleSheet("font-size: 24px; color: #888; font-weight: bold;letter-spacing: -15px;") #letter-spacing: -15px for making arrow with line and head.
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
        tab.setLayout(layout)
        return tab
    
    def create_popup_tab(self) -> QWidget:
        """Create popup settings tab"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,10,0,0)
        layout.setSpacing(12)
        
        # Window size settings group
        size_group = QGroupBox("Translation PopUp Size")
        size_layout = QVBoxLayout()
        size_layout.setSpacing(6)

        # Window size settings with custom radio buttons
        from PyQt5.QtWidgets import QRadioButton, QButtonGroup
        
        self.size_button_group = QButtonGroup()
        self.size_button_group.buttonClicked.connect(self.on_size_button_clicked)
        
        # Horizontal layout for radio buttons
        size_buttons_layout = QHBoxLayout()
        size_buttons_layout.setSpacing(10)
        
        # Small size option
        small_container = QWidget()
        small_layout = QVBoxLayout(small_container)
        small_layout.setSpacing(5)
        small_layout.setAlignment(Qt.AlignCenter)
        
        # Create a custom radio button container
        small_radio_container = QWidget()
        small_radio_container.setFixedSize(100, 120)
        small_radio_container.setStyleSheet(f"""
            QWidget {{
                border: none;
                border-radius: 8px;
                background-color: transparent;
            }}
            QWidget:hover {{
                border: 1px solid {COLORS['border']};
                background-color: {COLORS['secondary']};
            }}
        """)
        small_radio_container.setCursor(Qt.PointingHandCursor)
        
        # Add drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 70))
        small_radio_container.setGraphicsEffect(shadow)
        
        # Add star label inside the container
        small_star_label = QLabel("crop_16_9", small_radio_container)
        small_star_label.setFont(QFont("Material Symbols Rounded",12))
        small_star_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: normal; font-size: 12px;")
        small_star_label.setAlignment(Qt.AlignCenter)
        small_star_label.setGeometry(0, 0, 100, 80)
        
        # Add text label inside the container (alt kısım)
        small_text_label = QLabel("Small", small_radio_container)
        small_text_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: bold; font-size: 12px;")
        small_text_label.setAlignment(Qt.AlignCenter)
        small_text_label.setGeometry(0, 80, 100, 40)
        
        self.small_radio = QRadioButton()
        self.small_radio.setProperty("size", "small")
        self.small_radio.setFixedSize(100, 120)
        self.small_radio.setStyleSheet("""
            QRadioButton {
                border: none;
                background: transparent;
            }
            QRadioButton::indicator {
                width: 0px;
                height: 0px;
                border: none;
                background: transparent;
            }
        """)
        self.size_button_group.addButton(self.small_radio)
        
        # Overlay the radio button on the container
        small_layout.addWidget(small_radio_container, alignment=Qt.AlignCenter)
        self.small_radio.setParent(small_radio_container)
        self.small_radio.setGeometry(0, 0, 100, 120)
        
        size_buttons_layout.addWidget(small_container)
        
        # Default size option
        default_container = QWidget()
        default_layout = QVBoxLayout(default_container)
        default_layout.setSpacing(5)
        default_layout.setAlignment(Qt.AlignCenter)
        
        # Create a custom radio button container
        default_radio_container = QWidget()
        default_radio_container.setFixedSize(100, 120)
        default_radio_container.setStyleSheet(f"""
            QWidget {{
                border: none;
                border-radius: 8px;
                background-color: transparent;
            }}
            QWidget:hover {{
                border: 1px solid {COLORS['border']};
                background-color: {COLORS['secondary']};
            }}
        """)
        default_radio_container.setCursor(Qt.PointingHandCursor)
        
        # Add drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 70))
        default_radio_container.setGraphicsEffect(shadow)
        
        # Add star label inside the container
        default_star_label = QLabel("crop_16_9", default_radio_container)
        default_star_label.setFont(QFont("Material Symbols Rounded",32))
        default_star_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: normal; font-size: 32px;")
        default_star_label.setAlignment(Qt.AlignCenter)
        default_star_label.setGeometry(0, 0, 100, 80)
        
        # Add text label inside the container
        default_text_label = QLabel("Default", default_radio_container)
        default_text_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: bold; font-size: 12px;")
        default_text_label.setAlignment(Qt.AlignCenter)
        default_text_label.setGeometry(0, 80, 100, 40)
        
        self.default_radio = QRadioButton()
        self.default_radio.setProperty("size", "default")
        self.default_radio.setFixedSize(100, 120)
        self.default_radio.setStyleSheet("""
            QRadioButton {
                border: none;
                background: transparent;
            }
            QRadioButton::indicator {
                width: 0px;
                height: 0px;
                border: none;
                background: transparent;
            }
        """)
        self.size_button_group.addButton(self.default_radio)
        
        # Overlay the radio button on the container
        default_layout.addWidget(default_radio_container, alignment=Qt.AlignCenter)
        self.default_radio.setParent(default_radio_container)
        self.default_radio.setGeometry(0, 0, 100, 120)
        
        size_buttons_layout.addWidget(default_container)
        
        # Large size option
        large_container = QWidget()
        large_layout = QVBoxLayout(large_container)
        large_layout.setSpacing(5)
        large_layout.setAlignment(Qt.AlignCenter)
        
        # Create a custom radio button container
        large_radio_container = QWidget()
        large_radio_container.setFixedSize(100, 120)
        large_radio_container.setStyleSheet(f"""
            QWidget {{
                border: none;
                border-radius: 8px;
                background-color: transparent;
            }}
            QWidget:hover {{
                border: 1px solid {COLORS['border']};
                background-color: {COLORS['secondary']};
            }}
        """)
        large_radio_container.setCursor(Qt.PointingHandCursor)
        
        # Add drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 70))
        large_radio_container.setGraphicsEffect(shadow)
        
        # Add star label inside the container
        large_star_label = QLabel("crop_16_9", large_radio_container)
        large_star_label.setFont(QFont("Material Symbols Rounded",52))
        large_star_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: normal; font-size: 52px;")
        large_star_label.setAlignment(Qt.AlignCenter)
        large_star_label.setGeometry(0, 0, 100, 80)
        
        # Add text label inside the container
        large_text_label = QLabel("Large", large_radio_container)
        large_text_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: bold; font-size: 12px;")
        large_text_label.setAlignment(Qt.AlignCenter)
        large_text_label.setGeometry(0, 80, 100, 40)
        
        self.large_radio = QRadioButton()
        self.large_radio.setProperty("size", "large")
        self.large_radio.setFixedSize(100, 120)
        self.large_radio.setStyleSheet("""
            QRadioButton {
                border: none;
                background: transparent;
            }
            QRadioButton::indicator {
                width: 0px;
                height: 0px;
                border: none;
                background: transparent;
            }
        """)
        self.size_button_group.addButton(self.large_radio)
        
        # Overlay the radio button on the container
        large_layout.addWidget(large_radio_container, alignment=Qt.AlignCenter)
        self.large_radio.setParent(large_radio_container)
        self.large_radio.setGeometry(0, 0, 100, 120)
        
        size_buttons_layout.addWidget(large_container)
        
        size_layout.addLayout(size_buttons_layout)
        
        size_group.setLayout(size_layout)
        layout.addWidget(size_group)
        
        # Popup opening location settings group
        popup_location_group = QGroupBox("PopUp Opening Position")
        popup_location_layout = QVBoxLayout()
        popup_location_layout.setSpacing(6)
        
        popup_location_label = QLabel("Where to open translation window:")
        popup_location_layout.addWidget(popup_location_label)
        
        self.popup_opening_location_combo = QComboBox()
        self.popup_opening_location_combo.addItem("Open on cursor's monitor (centered)", "cursor")
        self.popup_opening_location_combo.addItem("Open below cursor", "cursor_below")
        self.popup_opening_location_combo.addItem("Always open on primary monitor", "primary")
        popup_location_layout.addWidget(self.popup_opening_location_combo)
        
        popup_location_group.setLayout(popup_location_layout)
        layout.addWidget(popup_location_group)
        
        layout.addStretch()
        tab.setLayout(layout)
        return tab
    
    def on_size_button_clicked(self, button):
        """Handle size button clicks to update styling"""
        # Get the container widgets (parent of radio buttons)
        small_container = self.small_radio.parent()
        default_container = self.default_radio.parent()
        large_container = self.large_radio.parent()
        
        # Reset all containers to default style
        for container in [small_container, default_container, large_container]:
            container.setStyleSheet(f"""
                QWidget {{
                    border: none;
                    border-radius: 8px;
                    background-color: transparent;
                }}
                QWidget:hover {{
                    border: 1px solid {COLORS['border']};
                    background-color: {COLORS['secondary']};
                }}
            """)
        
        # Update the selected button's container to blue border
        selected_container = button.parent()
        selected_container.setStyleSheet(f"""
            QWidget {{
                border: 1px solid {COLORS['accent']};
                border-radius: 8px;
                background-color: {COLORS['secondary']};
            }}
        """)

    def create_about_tab(self) -> QWidget:
        """Create about tab"""
        tab = QWidget()
        main_layout = QVBoxLayout(tab)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(12)

        # top area: left (title + version/author) and right (icon)
        top_layout = QHBoxLayout()
        top_layout.setSpacing(0)

        # left block (title and version/author)
        left_box = QVBoxLayout()
        left_box.setSpacing(20)
        title_label = QLabel(f"<p style='font-size:48px; font-weight:bold; font-family:Inter; color: #fff;'>{APP_NAME}</p>")
        left_box.addWidget(title_label)
        info_label = QLabel(
            f"<span style='font-size:12px; font-weight:600;'>Version:</span> "
            f"<span style='font-size:12px; font-style:italic;'>v{APP_VERSION}</span> "
            f"<span style='font-size:12px; font-weight:600;'>&nbsp;&nbsp;&nbsp;&nbsp;Author:</span> "
            f"<span style='font-size:12px;'>{APP_AUTHOR}</span>"
        )
        info_label.setStyleSheet("QLabel { margin-left: 5px; }")
        left_box.addWidget(info_label)
        left_box.addStretch()
        top_layout.addLayout(left_box, stretch=1)

        # right block (icon)
        icon_label = QLabel()
        icon_path = str((Path(__file__).parent.parent.parent / APP_ICON_PATH).resolve())
        pixmap = QPixmap(icon_path)
        pixmap = pixmap.scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("margin: 0px;")
        top_layout.addWidget(icon_label, stretch=0)

        main_layout.addLayout(top_layout)

        # bottom line
        hr = QFrame()
        hr.setFrameShape(QFrame.HLine)
        hr.setFrameShadow(QFrame.Sunken)
        hr.setFixedHeight(1)
        hr.setStyleSheet(f"background-color: {COLORS['border']}; color: {COLORS['border']}; height: 1px;")
        main_layout.addWidget(hr)

        # other content (github button, description, license etc.)
        main_layout.addSpacing(10)
        desc_label = QLabel(
            f"<b>About {APP_NAME}</b><br>"
            f"{APP_NAME} is a lightweight Python application for instant, real-time translation while you work."
            
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("font-size: 13px; margin-bottom: 8px;")
        main_layout.addWidget(desc_label)

        github_btn = QPushButton("GitHub Repository")
        github_btn.setCursor(Qt.PointingHandCursor)
        github_btn.setStyleSheet("font-weight: bold; padding: 8px 18px; font-size: 13px;")
        github_btn.clicked.connect(lambda: webbrowser.open(GITHUB_URL))
        main_layout.addWidget(github_btn, alignment=Qt.AlignLeft)

        # Add vertical spacing
        main_layout.addSpacing(50)

        license_label = QLabel(
            "<b>License:</b> MIT License<br>"
            "<span style='font-size:11px;color:#aaa;'>A short and simple permissive license with conditions only requiring preservation of copyright and license notices.</span>"
        )
        license_label.setStyleSheet(f"background:{COLORS['secondary']};padding:10px 14px;border-radius:6px;font-size:12px;")
        license_label.setWordWrap(True)
        main_layout.addWidget(license_label)

        # Google Translate service note
        service_note = QLabel(
            "<span style='color:rgba(255, 119, 0, 1);'><b>This tool uses Google Translate™ services with py-googletrans.</b><br></span>"
            "<span style='font-size:11px;color:rgba(255, 119, 0, 1);'>If translation does not work, it may be due to issues with Google Translate services or connectivity.</span>"
        )
        service_note.setStyleSheet("background:rgba(255, 119, 0, 0.1);padding:5px 10px;border-radius:6px;border: 2px dashed #ff7700;font-size:12px;")
        service_note.setWordWrap(True)
        service_note.setAlignment(Qt.AlignBottom)
        main_layout.addWidget(service_note)

        main_layout.addStretch()
        tab.setLayout(main_layout)
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
        self.restore_clipboard_cb.setChecked(self.config.get("restore_clipboard", False))
        
        # Popup opening location setting
        popup_opening_location = self.config.get("popup_opening_location", "cursor")
        # Handle legacy config key
        if popup_opening_location == "cursor" and "monitor_behavior" in self.config.config:
            popup_opening_location = self.config.get("monitor_behavior", "cursor")
        popup_index = self.popup_opening_location_combo.findData(popup_opening_location)
        if popup_index >= 0:
            self.popup_opening_location_combo.setCurrentIndex(popup_index)
        
        # Window size setting
        window_size = self.config.get("window_size", "default")
        if window_size == "small":
            self.small_radio.setChecked(True)
            # Update container styling
            self.small_radio.parent().setStyleSheet(f"""
                QWidget {{
                    border: 1px solid {COLORS['accent']};
                    border-radius: 8px;
                    background-color: {COLORS['secondary']};
                }}
            """)
        elif window_size == "large":
            self.large_radio.setChecked(True)
            # Update container styling
            self.large_radio.parent().setStyleSheet(f"""
                QWidget {{
                    border: 1px solid {COLORS['accent']};
                    border-radius: 8px;
                    background-color: {COLORS['secondary']};
                }}
            """)
        else:  # default
            self.default_radio.setChecked(True)
            # Update container styling
            self.default_radio.parent().setStyleSheet(f"""
                QWidget {{
                    border: 1px solid {COLORS['accent']};
                    border-radius: 8px;
                    background-color: {COLORS['secondary']};
                }}
            """)
    
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
            
            # Application settings - handle startup setting with error handling
            try:
                current_startup = self.config.get("start_on_boot", False)
                new_startup = self.start_on_boot_cb.isChecked()
                
                if current_startup != new_startup:
                    self.config.set("start_on_boot", new_startup)
                    
            except Exception as startup_error:
                self.logger.error(f"Failed to update startup setting: {startup_error}")
                # Show error message to user
                from PyQt5.QtWidgets import QMessageBox
                QMessageBox.warning(
                    self, 
                    "Startup Setting Error",
                    f"Failed to update Windows startup setting:\n{str(startup_error)}\n\nOther settings have been saved successfully."
                )
                # Revert checkbox to current config value
                self.start_on_boot_cb.setChecked(self.config.get("start_on_boot", False))
            
            self.config.set("save_history", self.save_history_cb.isChecked())
            self.config.set("restore_clipboard", self.restore_clipboard_cb.isChecked())
            
            # Popup opening location setting
            popup_opening_location = self.popup_opening_location_combo.currentData()
            self.config.set("popup_opening_location", popup_opening_location)
            
            # Remove legacy config key if it exists
            if "monitor_behavior" in self.config.config:
                del self.config.config["monitor_behavior"]
                self.config.save_config()
            
            # Window size setting
            if self.small_radio.isChecked():
                window_size = "small"
            elif self.large_radio.isChecked():
                window_size = "large"
            else:  # default_radio is checked
                window_size = "default"
            self.config.set("window_size", window_size)
            
            self.settings_changed.emit()
            self.close()
            
        except Exception as e:
            self.logger.error(f"Failed to save settings: {e}")
            # Show general error message
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.critical(
                self, 
                "Settings Error",
                f"Failed to save settings:\n{str(e)}"
            )
    
    def closeEvent(self, event):
        """Handle close event"""
        # Reset to original settings if not saved
        self.load_settings()
        super().closeEvent(event) 