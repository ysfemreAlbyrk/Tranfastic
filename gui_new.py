import customtkinter as ctk
from hPyT import *
import webbrowser
import logging as log
log = log.getLogger("GUI")
ctk.set_appearance_mode("dark")

import app
#--------------------------------------  main  ------------------------------
class WindowMain(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TransWrite - " + "connected")
        self.geometry("400x40+1000+500")
        self.resizable(1,1)
        maximize_minimize_button.hide(self)
        title_bar_color.set(self,"#222222")
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.show_widgets()
        self.attributes('-topmost', 1)
        # self.app = app.TranslatorApp(self)


    def show_widgets(self):
        self.input = ctk.CTkEntry(
            master=self,
            height=40,
            fg_color="#222222",
            border_width=0,
            corner_radius=0,
            placeholder_text= "Çevirilecek cümleyi yazın..."
            # activate_scrollbars=False, # this is for CTtextBox
        )
        self.input.focus()
        self.input.place(x=0,y=0, relwidth=1, relheight=1)


    def get_input(self):
        return self.input.get()

    def close_window(self):
        log.debug("...destroying window main...")
        self.destroy()


#--------------------------------------  settings  ------------------------------
class WindowSettings(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TransWrite - Settings")
        self.geometry("300x150+1400+650")
        self.resizable(1,1)
        maximize_minimize_button.hide(self)
        title_bar_color.set(self,"#222222")
        # self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.show_widgets()

    def show_widgets(self):
        # Create comboboxes
        self.create_combobox("Source", 0)
        self.create_combobox("Destination", 1)

        # Save button with command to print selected values
        ctk.CTkButton(
            master=self, 
            text="Save",
            font=("Material Symbols Rounded", 20),
            width=100,
            command=self.save_selection  # Assign the save function here
        ).pack(side="bottom", pady=10)


    def create_combobox(self, language_type, default_value):
        # Sample options for the combobox
        options = ["Auto", "English", "Turkish", "German", "Spanish"]

        # Create a frame to hold the buttons and label
        combo_frame = ctk.CTkFrame(master=self, fg_color="#242424")
        combo_frame.pack(side="top", pady=10,padx=15, fill="x")

        # Label for combobox
        ctk.CTkLabel(combo_frame, text=language_type + " Language:").pack(side="left", padx=0)

        # Create a StringVar for each combobox to store selected values
        if language_type == "Source":
            self.source_combobox_var = ctk.StringVar(value=options[default_value])
        else:
            self.destination_combobox_var = ctk.StringVar(value=options[default_value])

        # Create combobox with associated variable
        self.combobox = ctk.CTkComboBox(
            combo_frame,
            values=options,
            width=130,
            variable=(self.source_combobox_var if language_type == "Source" else self.destination_combobox_var)
        ).pack(side="right", padx=0)

    def save_selection(self):
        # Print the selected values of both comboboxes
        log.info(f"Source: {self.source_combobox_var.get()}")
        log.info(f"Destination: {self.destination_combobox_var.get()}")

    # def close_window(self):
    #     print("destroying window settings...")
    #     self.destroy()


#--------------------------------------  about  ------------------------------
class WindowAbout(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x150+2000+650")
        self.resizable(False,False)
        maximize_minimize_button.hide(self)
        self.title("TransWrite - About")
        title_bar_color.set(self,"#242424")
        # self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.show_widgets()
    
    def show_widgets(self):
        info_frame = ctk.CTkFrame(master=self, fg_color="#333333")
        info_frame.pack(side="top", padx=10, pady=10)
        self.quit_button = ctk.CTkButton(
            info_frame, 
            text="github",
            font=("arial", 16),
            width=80,
            command=lambda: webbrowser.open_new("http://subjectstudio.xyz")  
        ).pack(pady=30,padx=60)
    
        ctk.CTkLabel(master=self, text="Created by Yusuf Emre Albayrak with love ❤️").pack(side="bottom", fill="x")

    # def close_window(self):
    #     print("destroying window about...")
    #     self.destroy()
