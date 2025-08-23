"""
Appearance Settings Tab Module
Contains window size and popup position settings
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QGroupBox, QRadioButton, QButtonGroup, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

from ...utils.config import COLORS


class AppearanceTab(QWidget):
    """Appearance settings tab widget"""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.setup_ui()
    
    def setup_ui(self):
        """Setup appearance tab UI"""
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        layout.setSpacing(12)
        
        # Window size settings group
        size_group = QGroupBox("Translation PopUp Size")
        size_layout = QVBoxLayout()
        size_layout.setSpacing(6)

        # Window size settings with custom radio buttons
        self.size_button_group = QButtonGroup()
        self.size_button_group.buttonClicked.connect(self.on_size_button_clicked)
        
        # Horizontal layout for radio buttons
        size_buttons_layout = QHBoxLayout()
        size_buttons_layout.setSpacing(10)
        
        # Create size option containers
        self._create_small_size_option(size_buttons_layout)
        self._create_default_size_option(size_buttons_layout)
        self._create_large_size_option(size_buttons_layout)
        
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
        self.setLayout(layout)
    
    def _create_small_size_option(self, parent_layout):
        """Create small size radio button option"""
        small_container = QWidget()
        small_layout = QVBoxLayout(small_container)
        small_layout.setSpacing(5)
        small_layout.setAlignment(Qt.AlignCenter)
        
        # Create custom radio button container
        small_radio_container = QWidget()
        small_radio_container.setFixedSize(100, 120)
        small_radio_container.setStyleSheet(f"""
            QWidget {{
                border: 1px solid {COLORS['border']};
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
        
        # Add icon inside the container
        small_star_label = QLabel("crop_16_9", small_radio_container)
        small_star_label.setFont(QFont("Material Symbols Rounded", 12))
        small_star_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: normal; font-size: 12px;")
        small_star_label.setAlignment(Qt.AlignCenter)
        small_star_label.setGeometry(0, 0, 100, 80)
        
        # Add text label inside the container
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
        
        parent_layout.addWidget(small_container)
    
    def _create_default_size_option(self, parent_layout):
        """Create default size radio button option"""
        default_container = QWidget()
        default_layout = QVBoxLayout(default_container)
        default_layout.setSpacing(5)
        default_layout.setAlignment(Qt.AlignCenter)
        
        # Create custom radio button container
        default_radio_container = QWidget()
        default_radio_container.setFixedSize(100, 120)
        default_radio_container.setStyleSheet(f"""
            QWidget {{
                border: 1px solid {COLORS['border']};
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
        
        # Add icon inside the container
        default_star_label = QLabel("crop_16_9", default_radio_container)
        default_star_label.setFont(QFont("Material Symbols Rounded", 32))
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
        
        parent_layout.addWidget(default_container)
    
    def _create_large_size_option(self, parent_layout):
        """Create large size radio button option"""
        large_container = QWidget()
        large_layout = QVBoxLayout(large_container)
        large_layout.setSpacing(5)
        large_layout.setAlignment(Qt.AlignCenter)
        
        # Create custom radio button container
        large_radio_container = QWidget()
        large_radio_container.setFixedSize(100, 120)
        large_radio_container.setStyleSheet(f"""
            QWidget {{
                border: 1px solid {COLORS['border']};
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
        
        # Add icon inside the container
        large_star_label = QLabel("crop_16_9", large_radio_container)
        large_star_label.setFont(QFont("Material Symbols Rounded", 52))
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
        
        parent_layout.addWidget(large_container)
    
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
    
    def load_settings(self):
        """Load current settings into UI"""
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
    
    def get_settings(self):
        """Get current settings from UI"""
        # Window size setting
        if self.small_radio.isChecked():
            window_size = "small"
        elif self.large_radio.isChecked():
            window_size = "large"
        else:  # default_radio is checked
            window_size = "default"
        
        return {
            "popup_opening_location": self.popup_opening_location_combo.currentData(),
            "window_size": window_size
        }
