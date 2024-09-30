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
        self.master.geometry("300x300+1500+700")
        self.master.resizable(False,False)
        maximize_minimize_button.hide(self.master)
        self.master.title("writeLate - Settings")
        title_bar_color.set(self.master,"#242424")
        self.show_widgets()

    def show_widgets(self):
        self.quit_button = ctk.CTkButton(
            self.master, 
            text=f"Save",
            command=self.close_window).pack(side="bottom", padx=10, pady=20)
        self.create_combobox()


    def create_combobox(self):
        # Sample options for the combobox
        options = ["Auto","English", "Turkish", "German", "Spanish"]

        self.combobox_var_Language_src = ctk.StringVar(value=options[0])  # Default value for source language
        self.combobox_var_Language_dest = ctk.StringVar(value=options[1]) # Default value for destination language

        ctk.CTkLabel(self.master, text="Source Language:").pack()
        

        self.combobox_src = ctk.CTkComboBox(
            self.master,
            values=options,
            variable=self.combobox_var_Language_src,
            command=lambda event: print("src: "+ self.combobox_var_Language_src.get()) # in here first language detect
        ).pack(pady=(0,20))
        
        ctk.CTkLabel(self.master, text="Destination Language:").pack()

        self.combobox_dest = ctk.CTkComboBox(
            self.master,
            values=options,
            variable=self.combobox_var_Language_dest,
            command=lambda event: print("dest: "+self.combobox_var_Language_dest.get()) # in here first language detect
        ).pack(pady=(0,20))

        
    

root = ctk.CTk()  # Create the main window using customtkinter
app = WindowMain(root)
root.mainloop()
