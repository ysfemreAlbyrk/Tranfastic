import pystray
import PIL.Image
import gui_new

image = PIL.Image.open("./assets/icon_end.png")

current_window = None

def on_window_close():
    global current_window
    print("Window is being closed...")  
    current_window.destroy()
    current_window = None 

def open_window(window_class):
    global current_window
    
    print(f"Opening '{window_class.__name__}'")
    if current_window is not None:
        current_window.destroy()
        current_window = None
        
    current_window = window_class()
    current_window.protocol("WM_DELETE_WINDOW", on_window_close)
    current_window.mainloop()


# def open_settings():
#     print("settings opened")
#     settings_window = gui_new.WindowSettings()
#     settings_window.mainloop()

# def open_about():
#     print("about opened")
#     about_window = gui_new.WindowAbout()
#     about_window.mainloop()

# def open_main():
#     print("main opened")
#     main_window = gui_new.WindowMain()
#     main_window.mainloop()


def on_clicked(icon, item):
    if str(item) == "Settings":
        open_window(gui_new.WindowSettings)
    elif str(item) == "main":
        open_window(gui_new.WindowMain)
    elif str(item) == "About":
        open_window(gui_new.WindowAbout)
    elif str(item) == "Exit":
        global current_window
        if current_window is not None:
            current_window.destroy()
            current_window = None
        icon.stop()
    else:
        print(f'"{item}" item not implemented yet.')

icon  = pystray.Icon("writeLate", image,menu=pystray.Menu(
    pystray.MenuItem("main", on_clicked),
    pystray.MenuItem("Test", on_clicked),
    pystray.MenuItem("Settings", on_clicked),
    pystray.MenuItem("About", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

icon.run()