import keyboard
import pyperclip
import time
import pygetwindow as gw
import tray
import gui_new
import threading
import logging as log
log = log.getLogger("ShortcutHandler")

class ShortcutHandler:
    def __init__(self, hotkey='shift+alt+d'):
        self._hotkey = hotkey
        self.active_window = None
        self.running = True
        self.lock = threading.Lock()
        global hotkey_thread
        hotkey_thread = threading.Thread(target=self.start, args=(gui_new.WindowMain.get_input,))
        hotkey_thread.daemon = True
        self.thread = hotkey_thread
        hotkey_thread.start()

    def save_active_window(self):
        self.active_window = gw.getActiveWindow()
        log.info(f"Active window: {self.active_window.title if self.active_window else 'None'}")

    def paste_text(self, text):
        pyperclip.copy(text)
        time.sleep(0.2)  # Short delay before pasting
        if self.active_window:
            self.active_window.activate()
            time.sleep(0.2)  # Short delay for window transition
            keyboard.press_and_release('ctrl+v')

    def on_hotkey(self, show_input_dialog):
        log.info("==Hotkey triggered!==")
        self.save_active_window()
        tray.open_window(gui_new.WindowMain)

    def get_hotkey(self):
        return self._hotkey
    
    def set_hotkey(self, hotkey):
        self._hotkey = hotkey

    def start(self, show_input_dialog):
        try:
            keyboard.add_hotkey(self._hotkey, lambda: self.on_hotkey(show_input_dialog))
            log.info("Program is running. Shortcut: " + self._hotkey)
            
            while self.running:
                time.sleep(0.1)
                if not self.running:
                    break
                
        except Exception as e:
            log.error(f"hotkey_handler can't start: {e}")
        # finally:
        #     self.cleanup()

    def cleanup(self):
        try:
            keyboard.unhook_all()
            log.info("Keyboard hooks is removed")
        except:
            log.error("Keyboard hooks could not be removed")
    
    def stop(self):
        log.debug("...Shortcut handler is stopping...")
        try:
            with self.lock:
                self.running = False
                self.cleanup()
            
            # wait the thread's stopping
            if hasattr(self, 'thread') and self.thread.is_alive():
                self.thread.join(timeout=1)
        except Exception as e:
            log.error(f"Thread stopping error: {e}")
        finally:
            keyboard.unhook_all()  # Tüm keyboard hook'larını kaldır
            log.info("Shortcut handler is stopped")

    def get_thread_status(self):
        if hotkey_thread.is_alive() is True:
            log.info("thread is alive")
            return True
        else:
            log.info("thread is not alive")
            return False

