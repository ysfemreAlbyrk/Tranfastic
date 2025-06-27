import pystray
import PIL.Image
import gui_new
import threading
import time
import os
import logging as log
log = log.getLogger("Tray")

try:
    image = PIL.Image.open("./assets/icon.png")
except Exception as e:
    log.warning(f"Icon can't open: {e}")

current_window = None
icon = None
exit_flag = threading.Event()

def on_window_close():
    global current_window
    if current_window:
        current_window.destroy()
        current_window = None 

def open_window(window_class):
    global current_window
    
    if current_window is not None:
        current_window.destroy()
        current_window = None
        
    current_window = window_class()
    current_window.protocol("WM_DELETE_WINDOW", on_window_close)
    current_window.mainloop()

def cleanup():
    global current_window, shortcut_handler
    
    log.debug("...Cleanup is starting...")
    
    # stop the Shortcut Handler
    if shortcut_handler:
        try:
            shortcut_handler.stop()
            timeout = 3
            start_time = time.time()
            while shortcut_handler.get_thread_status() and (time.time() - start_time < timeout):
                time.sleep(0.1)
        except Exception as e:
            log.error(f"Shortcut handler stopping error: {e}")
    
    if current_window:
        try:
            current_window.quit()
            current_window = None
        except Exception as e:
            print(f"Window closing error: {e}")
    
    log.info("Cleanup is done.")

def force_exit():
    log.info("Application is closed successfully.\n")
    os._exit(0)

def exit_tray():
    global icon, exit_flag
    log.debug("...Application is closing...")
    cleanup()
    exit_flag.set()
    if icon:
        try:
            icon.stop()
        except Exception as e:
            log.error(f"Icon stopping error: {e}")
    # wait a few second and stop thread
    threading.Timer(0.5, force_exit).start()

def on_clicked(icon, item):
    try:
        if str(item) == "Settings":
            open_window(gui_new.WindowSettings)
        elif str(item) == "Shortcut Status":
            shortcut_handler.get_thread_status()
        elif str(item) == "About":
            open_window(gui_new.WindowAbout)
        elif str(item) == "Exit":
            exit_tray()
        else:
            log.warning(f'"{item}" item not implemented yet.')
    except Exception as e:
        log.error(f"Menu item clicking error: {e}")

icon = pystray.Icon("Tranfastic", image, menu=pystray.Menu(
    pystray.MenuItem("Shortcut Status", on_clicked), 
    pystray.MenuItem("Test", on_clicked),
    pystray.MenuItem('Show message', lambda icon, item: icon.notify('Hello World!')),
    pystray.MenuItem("Settings", on_clicked),
    pystray.MenuItem("About", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

def run_tray(shortcut_ref):
    global shortcut_handler
    shortcut_handler = shortcut_ref
    
    try:
        icon.run()
    except Exception as e:
        log.error(f"Icon can't run: {e}")
        cleanup()
        force_exit()