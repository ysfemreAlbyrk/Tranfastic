"""
Tranfastic Translation Window Module
Main translation interface window
"""

import sys
import logging
from typing import Optional, Callable
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
    QLabel, QPushButton, QApplication, QFrame, QShortcut, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread, pyqtSlot, QPoint
from PyQt5.QtGui import QFont, QIcon, QKeySequence, QPixmap, QColor, QCursor, QPalette
import ctypes
import time
from pathlib import Path

from ..utils.config import COLORS, APP_NAME, SUPPORTED_LANGUAGES, APP_ICON_PATH
from ..core.translator import translator_engine, save_translation_history

user32 = ctypes.windll.user32

class TranslationWorker(QThread):
    """Background translation worker"""
    translation_complete = pyqtSignal(str, str, bool)
    
    def __init__(self, text: str, source_lang: str, target_lang: str):
        super().__init__()
        self.text = text
        self.source_lang = source_lang
        self.target_lang = target_lang
    
    def run(self):
        """Run translation in background thread"""
        translated_text, detected_lang, success = translator_engine.translate(
            self.text, self.source_lang, self.target_lang
        )
        self.translation_complete.emit(translated_text, detected_lang, success)

class TranslationWindow(QWidget):
    """Main translation window"""
    
    def __init__(self, config, on_translation_complete: Optional[Callable] = None):
        super().__init__()
        self.config = config
        self.on_translation_complete = on_translation_complete
        self.logger = logging.getLogger(__name__)
        self.translation_worker: Optional[TranslationWorker] = None
        self._last_hwnd = None
        self._drag_pos = None
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Set window size based on config
        self.set_window_size()
        
        # Set window icon
        self.icon_path = str((Path(__file__).parent.parent.parent / APP_ICON_PATH).resolve())
        self.setWindowIcon(QIcon(self.icon_path))
        
        self.setup_ui()
        self.setup_shortcuts()
        self.update_title()
    
    def set_window_size(self):
        """Set window size based on configuration"""
        size_setting = self.config.get("window_size", "default")
        
        if size_setting == "small":
            self.setFixedSize(400, 60)
            self._adjust_ui_for_size("small")
        elif size_setting == "large":
            self.setFixedSize(600, 100)
            self._adjust_ui_for_size("large")
        else:  # default
            self.setFixedSize(500, 80)
            self._adjust_ui_for_size("default")
    
    def _adjust_ui_for_size(self, size):
        """Adjust UI elements based on window size"""
        if not hasattr(self, 'input_field') or not hasattr(self, 'title_label'):
            return  # UI not yet created
        
        # Use direct references instead of searching
        title_bar = self.title_bar
        main_widget = self.main_widget
        
        if size == "small":
            # Small size adjustments
            if title_bar:
                title_bar.setFixedHeight(20)
                # Update title bar style for small size
                title_bar.setStyleSheet(f"""
                    QWidget#title_bar {{
                        background-color: {COLORS['background']};
                        border-top-left-radius: 5px;
                        border-top-right-radius: 5px;
                        border: 1px solid #454545;
                        border-bottom: 1px solid #444;
                    }}
                """)
                # Update title bar layout margins
                title_layout = title_bar.layout()
                if title_layout:
                    title_layout.setContentsMargins(3, 0, 0, 0)
            
            if main_widget:
                # Update main widget border radius for small size
                main_widget.setStyleSheet(f"""
                    QWidget#main_widget {{
                        background-color: {COLORS['background']};
                        border-radius: 5px;
                        border: 1px solid #454545;
                    }}
                """)
            
            # Update icon size for small size
            self.icon_label.setPixmap(QPixmap(self.icon_path).scaled(15, 15, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
            # Update close button size for small size
            self.close_btn.setFixedSize(20, 20)
            self.close_btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #fff;
                    border: none;
                    font-size: 16px;
                    border-top-right-radius: 5px;
                }
                QPushButton:hover {
                    background: #e81123;
                    color: #fff;
                }
            """)
            
            self.input_field.setStyleSheet(f"""
                QLineEdit {{
                    background: transparent;
                    border: none;
                    color: {COLORS['text']};
                    font-size: 12px;
                    padding: 3px;
                }}
            """)
            self.title_label.setStyleSheet("color: #fff; font-weight: 600; font-size: 10px;")
            
        elif size == "large":
            # Large size adjustments
            if title_bar:
                title_bar.setFixedHeight(40)
                # Update title bar style for large size
                title_bar.setStyleSheet(f"""
                    QWidget#title_bar {{
                        background-color: {COLORS['background']};
                        border-top-left-radius: 15px;
                        border-top-right-radius: 15px;
                        border: 1px solid #454545;
                        border-bottom: 1px solid #444;
                    }}
                """)
                # Update title bar layout margins
                title_layout = title_bar.layout()
                if title_layout:
                    title_layout.setContentsMargins(8, 0, 0, 0)
            
            if main_widget:
                # Update main widget border radius for large size
                main_widget.setStyleSheet(f"""
                    QWidget#main_widget {{
                        background-color: {COLORS['background']};
                        border-radius: 15px;
                        border: 1px solid #454545;
                    }}
                """)
            
            # Update icon size for large size
            self.icon_label.setPixmap(QPixmap(self.icon_path).scaled(28, 28, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
            # Update close button size for large size
            self.close_btn.setFixedSize(40, 40)
            self.close_btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #fff;
                    border: none;
                    font-size: 32px;
                    border-top-right-radius: 15px;
                }
                QPushButton:hover {
                    background: #e81123;
                    color: #fff;
                }
            """)
            
            self.input_field.setStyleSheet(f"""
                QLineEdit {{
                    background: transparent;
                    border: none;
                    color: {COLORS['text']};
                    font-size: 16px;
                    padding: 8px;
                }}
            """)
            self.title_label.setStyleSheet("color: #fff; font-weight: 600; font-size: 14px;")
            
        else:  # default
            # Default size adjustments
            if title_bar:
                title_bar.setFixedHeight(30)
                # Update title bar style for default size
                title_bar.setStyleSheet(f"""
                    QWidget#title_bar {{
                        background-color: {COLORS['background']};
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        border: 1px solid #454545;
                        border-bottom: 1px solid #444;
                    }}
                """)
                # Update title bar layout margins
                title_layout = title_bar.layout()
                if title_layout:
                    title_layout.setContentsMargins(5, 0, 0, 0)
            
            if main_widget:
                # Update main widget border radius for default size
                main_widget.setStyleSheet(f"""
                    QWidget#main_widget {{
                        background-color: {COLORS['background']};
                        border-radius: 10px;
                        border: 1px solid #454545;
                    }}
                """)
            
            # Update icon size for default size
            self.icon_label.setPixmap(QPixmap(self.icon_path).scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
            # Update close button size for default size
            self.close_btn.setFixedSize(30, 30)
            self.close_btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #fff;
                    border: none;
                    font-size: 25px;
                    border-top-right-radius: 10px;
                }
                QPushButton:hover {
                    background: #e81123;
                    color: #fff;
                }
            """)
            
            self.input_field.setStyleSheet(f"""
                QLineEdit {{
                    background: transparent;
                    border: none;
                    color: {COLORS['text']};
                    font-size: 14px;
                    padding: 5px;
                }}
            """)
            self.title_label.setStyleSheet("color: #fff; font-weight: 600; font-size: 12px;")
    
    def setup_ui(self):
        """Setup user interface"""
        # Main background widget
        self.main_widget = QWidget(self)
        self.main_widget.setObjectName("main_widget")
        # Initial style will be set in _adjust_ui_for_size
        main_layout = QVBoxLayout(self.main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Custom title bar
        self.title_bar = QWidget()
        self.title_bar.setObjectName("title_bar")
        
        # Initial style will be set in _adjust_ui_for_size
        title_layout = QHBoxLayout(self.title_bar)
        # Initial margins will be set in _adjust_ui_for_size
        title_layout.setSpacing(8)

        # Left icon
        self.icon_label = QLabel()
        # Initial icon size will be set in _adjust_ui_for_size
        title_layout.addWidget(self.icon_label)

        # Dynamic title
        self.title_label = QLabel()
        # Initial style will be set in _adjust_ui_for_size
        title_layout.addWidget(self.title_label)

        title_layout.addStretch()

        # Close button
        # close_btn = QPushButton("\ue5cd")  # Material Symbols 'close' icon
        self.close_btn = QPushButton("Close")  # Material Symbols 'close' icon
        self.close_btn.setFont(QFont("Material Symbols Rounded"))
        # Initial size and style will be set in _adjust_ui_for_size
        self.close_btn.clicked.connect(self.close)
        title_layout.addWidget(self.close_btn)

        main_layout.addWidget(self.title_bar)

        # Sadece input
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Write something...")
        # Placeholder rengini değiştir
        palette = self.input_field.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(Qt.gray))  # Kırmızı
        self.input_field.setPalette(palette)
        # Initial style will be set in _adjust_ui_for_size
        self.input_field.returnPressed.connect(self.translate_text)
        self.input_field.textChanged.connect(self.on_text_changed)
        main_layout.addWidget(self.input_field)

        # Status label (hide, only for error)
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #F44336; font-size: 12px;")
        main_layout.addWidget(self.status_label)
        self.status_label.hide()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # Add margins for shadow
        layout.addWidget(self.main_widget)
        self.setLayout(layout)
        
        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 70))
        shadow.setOffset(0, 4)
        self.main_widget.setGraphicsEffect(shadow)
        
        self.center_window()
        
        # Apply size-based UI adjustments AFTER all UI elements are created
        self._adjust_ui_for_size(self.config.get("window_size", "default"))
    
    def setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        # ESC to close
        esc_shortcut = QShortcut(QKeySequence("Esc"), self)
        esc_shortcut.activated.connect(self.close)
        
        # Ctrl+Enter to translate
        ctrl_enter_shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        ctrl_enter_shortcut.activated.connect(self.translate_text)
    
    def center_window(self):
        """Position window based on popup opening location setting"""
        popup_location = self.config.get("popup_opening_location", "cursor")
        # Handle legacy config key
        if popup_location == "cursor" and "monitor_behavior" in self.config.config:
            popup_location = self.config.get("monitor_behavior", "cursor")
        
        if popup_location == "cursor":
            # Open on monitor where cursor is located (centered)
            cursor_pos = QCursor.pos()
            screen = QApplication.screenAt(cursor_pos)
        elif popup_location == "cursor_below":
            # Open 30px below cursor position
            cursor_pos = QCursor.pos()
            screen = QApplication.screenAt(cursor_pos)
            if screen:
                # Position window 30px below cursor
                x = cursor_pos.x() - (self.width() // 2)
                y = cursor_pos.y() + 30
                
                # Ensure window stays within screen bounds
                screen_geometry = screen.geometry()
                if x < screen_geometry.x():
                    x = screen_geometry.x()
                elif x + self.width() > screen_geometry.x() + screen_geometry.width():
                    x = screen_geometry.x() + screen_geometry.width() - self.width()
                
                if y + self.height() > screen_geometry.y() + screen_geometry.height():
                    y = cursor_pos.y() - self.height() - 10  # Place above cursor if not enough space below
                
                self.move(x, y)
                return
        elif popup_location == "primary":
            # Always open on primary monitor
            screen = QApplication.primaryScreen()
        else:
            # Fallback to primary monitor
            screen = QApplication.primaryScreen()
        
        if screen:
            screen_geometry = screen.geometry()
            x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2
            self.move(x, y)
        else:
            # Fallback to primary screen
            screen = QApplication.primaryScreen().geometry()
            x = (screen.width() - self.width()) // 2
            y = (screen.height() - self.height()) // 2
            self.move(x, y)
    
    def update_title(self):
        """Update window title with connection and language info"""
        if translator_engine.is_connected:
            status = "Connected"
        else:
            status = "Not Connected"
        source_lang = self.config.get("source_language", "auto")
        target_lang = self.config.get("target_language", "en")
        # If I need to write the long version(like English, Turkish, etc.) of the languages ​​in the future, I can use these 2 lines.
        # source_name = SUPPORTED_LANGUAGES.get(source_lang, source_lang.upper())
        # target_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang.upper())
        status_color = "#00ff00" if status == "Connected" else "#ff0000"
        title = f"Tranfastic - <span style='color:{status_color};'>{status}</span> <span style='color:#a7a7a7;'>| {source_lang} → {target_lang}</span>"
        self.title_label.setText(title)
    
    def on_text_changed(self, text: str):
        """Handle text input changes"""
        if not text.strip():
            self.status_label.setText("")
            self.status_label.setStyleSheet("")
    
    def translate_text(self):
        """Translate the entered text"""
        text = self.input_field.text().strip()
        if not text:
            return
        
        # Update status
        self.status_label.setText("Translating...")
        self.status_label.setStyleSheet("color: #FFC107;")
        
        # Get language settings
        source_lang = self.config.get("source_language", "auto")
        target_lang = self.config.get("target_language", "en")
        
        # Start translation in background
        self.translation_worker = TranslationWorker(text, source_lang, target_lang)
        self.translation_worker.translation_complete.connect(self.on_translation_complete_signal)
        self.translation_worker.start()
    
    @pyqtSlot(str, str, bool)
    def on_translation_complete_signal(self, translated_text: str, detected_lang: str, success: bool):
        """Handle translation completion"""
        if success:
            self.status_label.setText("Translation completed!")
            self.status_label.setStyleSheet("color: #4CAF50;")
            
            # History
            if self.config.get("save_history", False):
                source_lang = self.config.get("source_language", "auto")
                target_lang = self.config.get("target_language", "en")
                source_text = self.input_field.text().strip()
                save_translation_history(source_text, translated_text, source_lang, target_lang)
            
            # Call callback with translated text
            if self.on_translation_complete:
                self.on_translation_complete(translated_text)
            
            # Clear input and close after delay
            QTimer.singleShot(500, self.paste_to_last_window_and_close)
        else:
            self.status_label.setText("Translation failed!")
            self.status_label.setStyleSheet("color: #F44336;")
    
    def paste_to_last_window_and_close(self):
        """Clear input field and close window"""
        if self._last_hwnd:
            user32.SetForegroundWindow(self._last_hwnd)
            time.sleep(0.1)
            try:
                import keyboard
                keyboard.press_and_release('ctrl+v')
            except Exception as e:
                self.logger.error(f"Failed to simulate paste: {e}")
        self.input_field.clear()
        self.close()
    
    def showEvent(self, event):
        """Handle show event"""
        self._last_hwnd = user32.GetForegroundWindow()
        super().showEvent(event)
        self.input_field.setFocus()
        
        # Check connection status when window opens
        translator_engine._test_connection()
        self.update_title()
    
    def closeEvent(self, event):
        """Handle close event"""
        if self.translation_worker and self.translation_worker.isRunning():
            self.translation_worker.terminate()
            self.translation_worker.wait()
        super().closeEvent(event)

    # Dragable
    def mousePressEvent(self, event):
        # Get current title bar height based on window size
        size_setting = self.config.get("window_size", "default")
        if size_setting == "small":
            title_bar_height = 20
        elif size_setting == "large":
            title_bar_height = 40
        else:  # default
            title_bar_height = 30
            
        if event.button() == Qt.LeftButton and event.pos().y() <= title_bar_height:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None 