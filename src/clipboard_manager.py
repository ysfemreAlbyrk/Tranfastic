"""
Tranfastic Clipboard Manager Module
Handles clipboard operations for pasting translated text
"""

import logging
import time
from typing import Optional
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

class ClipboardManager:
    """Clipboard manager for Tranfastic"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.app = QApplication.instance()
        self._original_clipboard = ""
        self._restore_timer: Optional[QTimer] = None
    
    def paste_translation(self, translated_text: str, config=None, restore_after: int = 3000):
        """
        Paste translated text to clipboard and optionally restore original
        
        Args:
            translated_text: Text to paste
            config: Configuration object to check restore setting
            restore_after: Milliseconds to wait before restoring original clipboard
        """
        try:
            # Store original clipboard content
            self._original_clipboard = self.app.clipboard().text()
            
            # Set translated text to clipboard
            self.app.clipboard().setText(translated_text)
            
            self.logger.info(f"Pasted translation: {translated_text[:50]}...")
            
            # Simulate Ctrl+V to paste
            self._simulate_paste()
            
            # Restore original clipboard after delay if restore is enabled in config
            should_restore = config.get("restore_clipboard", False) if config else False
            if should_restore and restore_after > 0:
                self._schedule_restore(restore_after)
                self.logger.info("Clipboard restore scheduled")
            else:
                self.logger.info("Clipboard restore disabled")
                
        except Exception as e:
            self.logger.error(f"Failed to paste translation: {e}")
    
    def _simulate_paste(self):
        """Simulate Ctrl+V key press to paste clipboard content"""
        try:
            # Import here to avoid circular imports
            import keyboard
            
            # Small delay to ensure clipboard is set
            time.sleep(0.1)
            
            # Simulate Ctrl+V
            keyboard.press_and_release('ctrl+v')
            
            self.logger.info("Simulated Ctrl+V paste")
            
        except Exception as e:
            self.logger.error(f"Failed to simulate paste: {e}")
    
    def _schedule_restore(self, delay_ms: int):
        """Schedule clipboard restoration"""
        if self._restore_timer:
            self._restore_timer.stop()
        
        self._restore_timer = QTimer()
        self._restore_timer.timeout.connect(self._restore_clipboard)
        self._restore_timer.start(delay_ms)
    
    def _restore_clipboard(self):
        """Restore original clipboard content"""
        try:
            if self._original_clipboard:
                self.app.clipboard().setText(self._original_clipboard)
                self.logger.info("Restored original clipboard content")
                self._original_clipboard = ""
            
            if self._restore_timer:
                self._restore_timer.stop()
                self._restore_timer = None
                
        except Exception as e:
            self.logger.error(f"Failed to restore clipboard: {e}")
    
    def get_clipboard_text(self) -> str:
        """Get current clipboard text"""
        try:
            return self.app.clipboard().text()
        except Exception as e:
            self.logger.error(f"Failed to get clipboard text: {e}")
            return ""
    
    def set_clipboard_text(self, text: str):
        """Set clipboard text"""
        try:
            self.app.clipboard().setText(text)
            self.logger.info(f"Set clipboard text: {text[:50]}...")
        except Exception as e:
            self.logger.error(f"Failed to set clipboard text: {e}")
    
    def clear_restore_timer(self):
        """Clear clipboard restore timer"""
        if self._restore_timer:
            self._restore_timer.stop()
            self._restore_timer = None

# Global clipboard manager instance
clipboard_manager = ClipboardManager() 