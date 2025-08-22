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
from PyQt5.QtGui import QFont, QIcon, QKeySequence, QPixmap, QColor, QCursor
import ctypes
import time
from pathlib import Path

from ..utils.config import COLORS, APP_NAME, SUPPORTED_LANGUAGES
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
        self.setFixedSize(500, 80)  # Increased size to accommodate shadow
        
        # Set window icon
        icon_path = str((Path(__file__).parent.parent / "../assets/icon.png").resolve())
        self.setWindowIcon(QIcon(icon_path))
        
        self.setup_ui()
        self.setup_shortcuts()
        self.update_title()
    
    def setup_ui(self):
        """Setup user interface"""
        # Main background widget
        main_widget = QWidget(self)
        main_widget.setObjectName("main_widget")
        main_widget.setStyleSheet(f"""
            QWidget#main_widget {{
                background-color: {COLORS['background']};
                border-radius: 10px;
                border: 1px solid #454545;
            }}
        """)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Custom title bar
        title_bar = QWidget()
        title_bar.setObjectName("title_bar")
        title_bar.setFixedHeight(30)
        title_bar.setStyleSheet(f"""
            QWidget#title_bar {{
                background-color: {COLORS['background']};
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                border: 1px solid #454545;
                border-bottom: 1px solid #444;
            }}
        """)
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(5, 0, 0, 0)
        title_layout.setSpacing(8)

        # Left icon
        icon_label = QLabel()
        icon_path = str((Path(__file__).parent.parent / "../assets/icon.png").resolve())
        icon_label.setPixmap(QPixmap(icon_path).scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        title_layout.addWidget(icon_label)

        # Dynamic title
        self.title_label = QLabel()
        self.title_label.setStyleSheet("color: #fff; font-weight: 600; font-size: 12px;")
        title_layout.addWidget(self.title_label)

        title_layout.addStretch()

        # Close button
        # close_btn = QPushButton("\ue5cd")  # Material Symbols 'close' icon
        close_btn = QPushButton("Close")  # Material Symbols 'close' icon
        close_btn.setFont(QFont("Material Symbols Rounded"))
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
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
        close_btn.clicked.connect(self.close)
        title_layout.addWidget(close_btn)

        main_layout.addWidget(title_bar)

        # Sadece input
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Write something...")
        self.input_field.setStyleSheet(f"""
            QLineEdit {{
                background: transparent;
                border: none;
                color: {COLORS['text']};
                font-size: 14px;
                padding: 5px;
            }}
        """)
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
        layout.addWidget(main_widget)
        self.setLayout(layout)
        
        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 70))
        shadow.setOffset(0, 4)
        main_widget.setGraphicsEffect(shadow)
        
        self.center_window()
    
    def setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        # ESC to close
        esc_shortcut = QShortcut(QKeySequence("Esc"), self)
        esc_shortcut.activated.connect(self.close)
        
        # Ctrl+Enter to translate
        ctrl_enter_shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        ctrl_enter_shortcut.activated.connect(self.translate_text)
    
    def center_window(self):
        """Center window on screen based on monitor behavior setting"""
        monitor_behavior = self.config.get("monitor_behavior", "cursor")
        
        if monitor_behavior == "cursor":
            # Open on monitor where cursor is located
            cursor_pos = QCursor.pos()
            screen = QApplication.screenAt(cursor_pos)
        elif monitor_behavior == "primary":
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
        if event.button() == Qt.LeftButton and event.pos().y() <= 36:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None 