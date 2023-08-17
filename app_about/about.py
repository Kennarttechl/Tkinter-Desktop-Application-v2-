from tkinter import *
import customtkinter
from app_url_link.url_link import connect
from app_image_utils.image_utils import get_ctk_image


def about_(self):
    customtkinter.set_appearance_mode('dark')

    self.about = customtkinter.CTkToplevel()
    self.about.transient(self)
    self.about.minsize(400, 400)
    self.about.title('About Page')
    self.about.geometry('550x400+400+150')

    self.about.columnconfigure(0, weight=1, uniform='a')
    self.about.columnconfigure(1, weight=0)
    self.about.rowconfigure(1, weight=1)

    data = {
        "app_description": {
            "About the application": "\n*-----------------------*",
            "App_name": "My Application(POS)",
            "Version": "2.0.0",
            "Author": "Kennart-Tech Software",
            "Description": "A custom modern GUI",
            "License": "MIT",
            "Author_email": "kennartfoundation@gmail.com"
        }
    }

    json_data = ''
    
    for key, value in data['app_description'].items():
        json_data += f"{key}: {value}\n\n"

    self.default_textbox = customtkinter.CTkTextbox(self.about, width=200, font=('Times', 20),
                                                    text_color='gray80', corner_radius=10,
                                                    scrollbar_button_hover_color='#16FF00')
    self.default_textbox.grid(row=1, column=0, padx=(30, 30), pady=(30, 25), sticky="nsew")
    self.default_textbox.insert(END, json_data)  # Insert the formatted data into the Text widget
    self.default_textbox.configure(state='disabled')

    self.footer_frame = customtkinter.CTkFrame(self.about, border_width=0.6, corner_radius=4,
                                               border_color='gray10', fg_color='gray25',)
    self.footer_frame.grid(row=2, column=0, ipady=1, sticky=EW)
    self.footer_frame.grid_columnconfigure((0, 1, 2), weight=1)

    self.footer_text = customtkinter.CTkLabel(self.footer_frame, text='Develop by [Kennart-Tech]',
                                              font=customtkinter.CTkFont('Sans', 12))
    self.footer_text.grid(row=1, column=1, pady=2)

    self.link = customtkinter.CTkLabel(self.footer_frame, text_color='#00bfff',
                                       image=get_ctk_image(icon='web', size=25),
                                       text=' Click To Report Issues Here!',
                                       corner_radius=10, width=2, compound='left',
                                       font=customtkinter.CTkFont('Roboto bold', 13))
    self.link.grid(row=1, column=2, padx=(50, 45), pady=(3, 1), sticky="nsew")
    self.link.bind("<Button-1>", connect)
    self.link.bind("<Enter>", lambda event: self.link.configure(font=("",13,"underline"), cursor="hand2"))
    self.link.bind("<Leave>", lambda event: self.link.configure(font=("",13), cursor="arrow"))


