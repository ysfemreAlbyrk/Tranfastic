"""
Tranfastic Hotkey Manager Module
Handles global keyboard shortcuts using Windows API and PyQt5 native event filter
"""

import ctypes
from PyQt5.QtCore import QAbstractNativeEventFilter, QObject, pyqtSignal, QCoreApplication
import logging

user32 = ctypes.windll.user32

# Modifier key codes
MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
MOD_WIN = 0x0008

# Virtual key codes
VK_CODE = {
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 'g': 0x47, 'h': 0x48, 'i': 0x49, 'j': 0x4A,
    'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E, 'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53, 't': 0x54,
    'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58, 'y': 0x59, 'z': 0x5A,
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39
}

class MSG(ctypes.Structure):
    _fields_ = [
        ("hwnd", ctypes.c_void_p),
        ("message", ctypes.c_uint),
        ("wParam", ctypes.c_uint),
        ("lParam", ctypes.c_uint),
        ("time", ctypes.c_uint),
        ("pt_x", ctypes.c_long),
        ("pt_y", ctypes.c_long)
    ]

class HotkeyEventFilter(QAbstractNativeEventFilter):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def nativeEventFilter(self, eventType, message):
        msg = MSG.from_address(message.__int__())
        if msg.message == 0x0312:  # WM_HOTKEY
            if self.callback:
                self.callback()
        return False, 0

class HotkeyManager(QObject):
    hotkey_triggered = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self._callback = None
        self._current_hotkey = "shift+alt+d"
        self._event_filter = None
        self._registered = False
        self._hotkey_id = 1

    def set_callback(self, callback):
        self._callback = callback
        try:
            self.hotkey_triggered.disconnect()
        except TypeError:
            pass  # Already disconnected
        self.hotkey_triggered.connect(self._callback)

    def set_hotkey(self, hotkey: str) -> bool:
        if self._registered:
            self.unregister_hotkey()
        self._current_hotkey = hotkey
        return self.register_hotkey()

    def register_hotkey(self) -> bool:
        mod, vk = self._parse_hotkey(self._current_hotkey)
        if mod is None or vk is None:
            self.logger.error(f"Invalid hotkey: {self._current_hotkey}")
            return False
        if not user32.RegisterHotKey(None, self._hotkey_id, mod, vk):
            self.logger.error(f"Failed to register hotkey: {self._current_hotkey}")
            return False
        self._registered = True
        self.logger.info(f"Hotkey registered: {self._current_hotkey}")
        if not self._event_filter:
            self._event_filter = HotkeyEventFilter(lambda: self.hotkey_triggered.emit())
            QCoreApplication.instance().installNativeEventFilter(self._event_filter)
        return True

    def unregister_hotkey(self):
        if self._registered:
            user32.UnregisterHotKey(None, self._hotkey_id)
            self._registered = False
            self.logger.info("Hotkey unregistered")

    def cleanup(self):
        self.unregister_hotkey()
        if self._event_filter:
            QCoreApplication.instance().removeNativeEventFilter(self._event_filter)
            self._event_filter = None

    def _parse_hotkey(self, hotkey: str):
        parts = hotkey.lower().split('+')
        mod = 0
        key = None
        for part in parts:
            if part == 'shift':
                mod |= MOD_SHIFT
            elif part == 'ctrl' or part == 'control':
                mod |= MOD_CONTROL
            elif part == 'alt':
                mod |= MOD_ALT
            elif part == 'win':
                mod |= MOD_WIN
            elif part in VK_CODE:
                key = VK_CODE[part]
        return (mod, key)

    @property
    def current_hotkey(self):
        return self._current_hotkey

# Global hotkey manager instance
hotkey_manager = HotkeyManager() 