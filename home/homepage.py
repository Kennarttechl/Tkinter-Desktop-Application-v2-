"""This are built-in modules, which are part of the Python
Standard Library"""
import sys
import json
import tkinter
import sqlite3
import hashlib
from tkinter import *
from tkinter import Menu
from datetime import datetime

"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox

"""This are local modules created by me and are part of the project"""
import app_about.about as about
from app_url_link.url_link import Messages
from admin.admin_dashboard import Adminsuper
from user__dashboard.dashboard import Dashboard
from app_database.database import resource_path
from user_logins.forget_password import Passwordreset
from app_image_utils.image_utils import get_ctk_image
from expired.trial_days_30 import check_trial_status


class Homepage(customtkinter.CTkToplevel):
    """This `class` defines the homepage, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme("green")

    """Using contex manager to load json file that is use the home page"""
    Text = 'config/settings.json'
    
    with open(file=Text, mode='r', encoding='utf-8') as rf:
        text = json.load(rf)

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.minsize(620, 600)
        self.title('Homepage')
        # self.iconbitmap("icons/logo.ico") 
        self.geometry(f"{500}x{500}+{120}+{80}")
        self.after(1, lambda: self.state('zoomed'))
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.columnconfigure(1, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        self.font = ("MusticaPro-SemiBold", 15)

        self.menu = Menu(self)
        self.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, activebackground=self.text
                             ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label='File', menu = self.filename)
        self.filename.add_command(label = 'Exit', accelerator = 'Ctrl+E', 
                                  command=self.on_close)

        self.option_menu = Menu(self.menu, tearoff=0, activebackground=self.text
                                ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label = "Help", menu = self.option_menu)
        
        self.option_menu.add_command(label = 'About', accelerator='Ctrl+B', 
                                     command=self.about_page)
        self.option_menu.add_separator()
        self.option_menu.add_command(label = 'Check for Update', command=self.appupdate)

        self.background_image = PhotoImage(file='icons/large.png')
        self.background_label = Label(master=self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.frame=customtkinter.CTkFrame(master=self.background_label, width=400, 
                                          height=440, corner_radius=4, fg_color='gray24')
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


        self.lock_image = customtkinter.CTkLabel(master=self.frame, text="", 
                                            image=get_ctk_image(icon='user', size=75))
        self.lock_image.place(relx=0.5, y=50, anchor=tkinter.CENTER)

        self.title_lable = customtkinter.CTkLabel(master=self.frame,
                                             text='Login into your account',
                                             font=customtkinter.CTkFont('Sans',  22))
        self.title_lable.place(relx=0.5, y=110, anchor=tkinter.CENTER)


        self.user_name = customtkinter.CTkEntry(master=self.frame, width=220,
                                                height=32, font=('Sans', 14),
                                                placeholder_text='Enter your username')
        self.user_name.place(relx=0.5, y=155, anchor=tkinter.CENTER)


        self.user_pass = customtkinter.CTkEntry(master=self.frame, width=220, 
                                                height=32, show='****', font=('Sans', 14),
                                                placeholder_text='Enter your password')
        self.user_pass.place(relx=0.5, y=215, anchor=tkinter.CENTER)


        self.login_btn = customtkinter.CTkButton(master=self.frame, text='Login', 
                                            width=220, height=32,corner_radius=5,
                                            font=customtkinter.CTkFont('Sans', 13),
                                            hover_color=('#3CCF4E'), fg_color='transparent',
                                            border_color='gray40', border_width=0.6,
                                            command=self.masterlog)
        self.login_btn.place(relx=0.5, y=277, anchor=tkinter.CENTER)


        self.expired_label = customtkinter.CTkLabel(master=self.frame, font=self.font,
                                                    text='Your 30-days trial has expired')
        self.expired_label.place(relx=0.5, y=310, anchor=tkinter.CENTER)


        self.alternative_btn = customtkinter.CTkButton(master=self.frame, 
                                                  text='Login With Google Mail', 
                                                  width=220, height=32,corner_radius=5, 
                                                  image=get_ctk_image(icon='Google', size=17),
                                                  font=customtkinter.CTkFont('Sans', 13),
                                                  hover_color=('#3CCF4E'), 
                                                  compound='left', border_width=0.6, 
                                                  fg_color=('gray7', 'gray30'),
                                                  border_color='gray40',
                                                  command=self.notavailable)
        self.alternative_btn.place(relx=0.5, y=343, anchor=tkinter.CENTER)


        self.forgot_password = customtkinter.CTkButton(master=self.frame, 
                                                  text='Forgot password', width=83,
                                                  height=20, corner_radius=5,
                                                  font=customtkinter.CTkFont('Sans', 16),
                                                  hover_color=('gray70', 'gray30'),
                                                  fg_color='transparent',
                                                  border_color='gray40',
                                                  command=self.resetpassword)
        self.forgot_password.place(relx=0.5, y=385, anchor=tkinter.CENTER)
        self.deactivate_login_button()

        self.bind('<Control-e>', self.on_close)
        self.bind('<Control-E>', self.on_close)
        self.bind('<Control-b>', self.about_page)
        self.bind('<Control-B>', self.about_page)

    def deactivate_login_button(self):
        expired = check_trial_status()
        current_date = datetime.now().date()
        trial_start_date = datetime(2023, 7, 2).date()

        if current_date < trial_start_date or expired:
            self.login_btn.configure(state='disable')
            self.expired_label.configure(text_color='#F2B705')
        else:
            self.expired_label.configure(text='')

    def on_close(self, *event):
        sys.exit()

    def resetpassword(self):
        Passwordreset(self)

    def about_page(self, *event)-> None:
        about.about_(self)

    def notavailable(self):
        Messages('info.ico', 'Unavailable',
                 'Sorry this option is not available yet', timeout=1)
        # CTkMessagebox(title='Unavailable',
        #               message='Sorry this option is not available yet',
        #               icon='info', option_1='Close')

    def appupdate(self)-> None:
        Messages('info.ico', 'SwitfShell', 
                 'There are currently no updates is available', timeout=1)
        # CTkMessagebox(title='SwitfShell', 
        #               message='There are currently no updates is available',
        #               icon='info', option_1='Close')
        
    def reset_entry(self):
        self.user_name.delete(0, 10)
        self.user_pass.delete(0, 100)

    def masterlog(self):
        try:
            username = self.user_name.get()
            password = self.user_pass.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if username == '' or password == '':
                CTkMessagebox(title='SwiftSell', message='Empty field is not allowed',
                              icon='warning', option_1='Ok')  
                return
            
            expired = check_trial_status()
            current_date = datetime.now().date()
            trial_start_date = datetime(2023, 7, 2).date()

            if current_date < trial_start_date or expired:
                Messages(icon_name='warning.ico', title='Trial Expired',
                         message='Your 30-days trial has expired',  timeout=1)
                
                # return

            connection = sqlite3.connect(resource_path('data__/register.db'))
            conn = connection.cursor()
            conn.execute("SELECT * FROM ds_register WHERE username=? AND password=?", 
                        (username, hashed_password))
            result = conn.fetchone()

            # Check if the logged in user is an admin
            conn.execute("SELECT * FROM ds_register WHERE username=? AND user_role=?", 
                        (username, 'Admin'))
            is_admin = conn.fetchone() is not None
            connection.close()

            if result is not None:
                if is_admin:
                    self.withdraw()
                    self.iconify()
                    self.withdraw()
                    Adminsuper(self)
                    self.reset_entry()
                    CTkMessagebox(title='Login Successful', message=f'Welcome.. {username}',
                                  icon='check', option_1='Ok')
                else:
                    Dashboard(self)
                    self.iconify()
                    self.withdraw()
                    self.reset_entry()
                    CTkMessagebox(title='Login Successful', message=f'Welcome.. {username}', 
                                  icon='check', option_1='Ok')
            else:
                CTkMessagebox(title='Error', message='Invalid username or password',
                              icon='cancel', option_1='Ok')
        except:
            CTkMessagebox(title='Connection Error', message='There was a problem connecting\
                            to the Database!! Contact your system Admin',
                            icon='cancel', option_1='Try again')

            

# def Main():
#     mm = Homepage()
#     mm.title('Homepage')
#     mm.mainloop()

# if __name__ == "__main__":
#     app = Main()

# #617ca6 =violet
#8000d7
#1e0032 radius
#772397
#bf8095
