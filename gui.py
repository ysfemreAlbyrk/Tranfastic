import customtkinter as ctk  # Import customtkinter
from hPyT import *
ctk.set_appearance_mode("dark")
class WindowMain:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x40+1000+500")
        self.master.resizable(False,False)
        maximize_minimize_button.hide(self.master)
        title_bar_color.set(self.master,"#222222")
        self.show_widgets()
        self.settings_window = None

    def show_widgets(self):
        self.master.title("writeLate - " + "connected")
        self.create_input()
        self.create_button("SETTINGS", WindowSettings)

    def create_input(self):
        ctk.CTkEntry(  # Use CTkEntry
            self.master, 
            placeholder_text="Çevirilecek cümleyi yazın.",
            width=358,
            height=40,
            border_width=0,
            corner_radius=0,
            fg_color="#222222"
        ).place(x=0,y=0)

    def create_button(self, text, _class):
        ctk.CTkButton(  # Use CTkButton
            self.master,
            text="SETTINGS",
            font=("Material Symbols Rounded",20),
            width= 40,
            height=40,
            corner_radius=7,
            border_width=0,
            command=lambda: self.new_window(_class)).pack(side="right")

    def new_window(self, _class):
        global windowSettings

        try:
            if _class == WindowSettings:
                if windowSettings.state() == "normal":
                    windowSettings.focus()
        except:
            windowSettings = ctk.CTkToplevel(self.master)  # Use CTkToplevel
            _class(windowSettings)

    def close_window(self):
        self.master.destroy()

#--------------------------------------  settings  ------------------------------
class WindowSettings(WindowMain):
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x150+1500+700")
        self.master.resizable(False,False)
        maximize_minimize_button.hide(self.master)
        self.master.title("writeLate - Settings")
        title_bar_color.set(self.master,"#242424")
        self.show_widgets()

    def show_widgets(self):
        # Create comboboxes
        self.create_combobox("Source", 0)
        self.create_combobox("Destination", 1)

        # Create a frame to hold the buttons
        button_frame = ctk.CTkFrame(self.master, fg_color="#242424")
        button_frame.pack(side="bottom", padx=10, pady=10)

        # Save button with command to print selected values
        self.quit_button = ctk.CTkButton(
            button_frame, 
            text="Save",
            font=("Material Symbols Rounded", 20),
            width=80,
            command=self.save_selection  # Assign the save function here
        ).pack(side="left", padx=10)
        
        self.info_button = ctk.CTkButton(
            button_frame,
            text="info", 
            font=("Material Symbols Rounded", 20),
            width=30,
            command=self.save_selection 
        ).pack(side="right", padx=10) 

    def create_combobox(self, language_type, default_value):
        # Sample options for the combobox
        options = ["Auto", "English", "Turkish", "German", "Spanish"]

        # Create a frame to hold the buttons and label
        combo_frame = ctk.CTkFrame(self.master, fg_color="#242424")
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
        print(f"Source: {self.source_combobox_var.get()}")
        print(f"Destination: {self.destination_combobox_var.get()}")



root = ctk.CTk()  # Create the main window using customtkinter
app = WindowMain(root)
root.mainloop()
