import pystray
import PIL.Image
import gui_new
import threading
import sys

# ------------------------------------- tray ------------------------------------
image = PIL.Image.open("./assets/icon_end.png")

# Global pencere referansı, bu her seferinde açılan pencereyi tutar
current_window = None

def open_window(window_class):
    global current_window
    
    # Eğer mevcut bir pencere açıksa, önce onu kapat
    if current_window is not None:
        current_window.quit()
        current_window = None

    # Yeni pencereyi oluştur ve referansı kaydet
    current_window = window_class()
    current_window.mainloop()

# def open_settings():
#     settings_window = gui_new.WindowSettings()
#     settings_window.mainloop()

# def open_about():
#     about_window = gui_new.WindowAbout()
#     about_window.mainloop()

def on_clicked(icon, item):
    if str(item) == "Settings":
        threading.Thread(target=lambda: open_window(gui_new.WindowSettings)).start()
    elif str(item) == "About":
        threading.Thread(target=lambda: open_window(gui_new.WindowAbout)).start()
    elif str(item) == "Exit":
        icon.stop()
    else:
        print(f'"{item}" item not implemented yet.')


icon  = pystray.Icon("writeLate", image,menu=pystray.Menu(
    pystray.MenuItem("Settings", on_clicked),
    pystray.MenuItem("About", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

icon.run()