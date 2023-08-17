"""This are built-in modules, which are part of the 
Python Standard Library"""
import json
import datetime
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""This are local modules created by me and are 
part of my project"""
import app_database.database as database


class UserData():
    def __init__(self, master):
        self.master = master
        self.date = datetime.datetime.now().date()

        with open(file='config/about.json', mode='r', encoding='utf-8') as rf:
            self.user_data = json.load(rf)

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.userdata = customtkinter.CTkToplevel(master)
        self.userdata.withdraw()
        self.userdata.transient(master)
        self.userdata.title('New Data')
        self.userdata.minsize(900, 450)
        self.userdata.geometry('720x450+265+130')
        self.userdata.after(500, self.userdata.deiconify)

        self.userdata.columnconfigure(0, weight=1, uniform='a')
        self.userdata.rowconfigure((1, 2), weight=1, uniform='a')

        self.create_gui()

    def create_gui(self):
        self.top_frame = customtkinter.CTkFrame(self.userdata, border_width=0.7,
                                                border_color='gray20',
                                                corner_radius=3, height=35)
        self.top_frame.grid(row=0, column=0, ipady=3, sticky=NSEW)
        self.top_frame.grid_columnconfigure((1, 2), weight=1)

        self.data_frame = customtkinter.CTkFrame(self.userdata, width=400,
                                                 height=500, corner_radius=5)
        self.data_frame.grid(row=1, column=0, padx=(10, 10), rowspan=4, pady=(10, 15),
                             sticky=NSEW)
        self.data_frame.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.data_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')

        self.item_sales = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                                 height=32, font=('Sans', 14),
                                                 placeholder_text='Item sold')
        self.item_sales.grid(row=0, column=1, padx=(10, 0), pady=(2, 2))

        self.quantity = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                                height=32, font=('Sans', 14),
                                               placeholder_text='Quantity')
        self.quantity.grid(row=0, column=2, padx=(10, 0), pady=(2, 2))


        self.price = customtkinter.CTkEntry(master=self.data_frame,width=320,
                                            height=32, font=('Sans', 14),
                                            placeholder_text=' Price')
        self.price.grid(row=0, column=3, padx=(10, 0), pady=(2, 2))


        self.amount_paid = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                  height=32, font=('Sans', 14),
                                                  placeholder_text='Amount paid')
        self.amount_paid.grid(row=0, column=4, padx=(10, 0), pady=(2, 2))


        self.balance_left = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                   height=32, font=('Sans', 14),
                                                   placeholder_text='Balance',)
        self.balance_left.grid(row=1, column=1, padx=(10, 0), pady=(2, 2))


        self.served_by = customtkinter.CTkEntry(master=self.data_frame,width=320, 
                                                height=32, font=('Sans', 14),
                                                placeholder_text='Served By')
        self.served_by.grid(row=1, column=2, padx=(10, 0), pady=(2, 2))


        self.contact = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, font=('Sans', 13),
                                              placeholder_text='Customer Contact')
        self.contact.grid(row=1, column=3, padx=(10, 0), pady=(2, 2))

        self.save_data_option = customtkinter.CTkFrame(master=self.data_frame, width=10,
                                                  height=10, corner_radius=5)
        self.save_data_option.grid(row=0, column=6, padx=(1, 10), rowspan=3,
                              columnspan=2, pady=(10, 15), sticky=NSEW)
        self.save_data_option.grid_columnconfigure((1), weight=1, uniform='a')
        self.save_data_option.grid_rowconfigure((0, 1, 2,), weight=1, uniform='a')

        self.data_save = customtkinter.CTkButton(master=self.save_data_option, text='Save Data',
                                            width=80, height=28, corner_radius=4,
                                            hover_color=('gray70', 'gray30'),
                                            command=self.send_request)
        self.data_save.grid(row=0, column=1, padx=(0, 8), pady=(10, 0))


        self.data_cancel = customtkinter.CTkButton(master=self.save_data_option, 
                                                   text='Reset Entry',
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.reset_entry)
        self.data_cancel.grid(row=1, column=1, padx=(0, 8), pady=(10, 0))


        self.data_cancel = customtkinter.CTkButton(master=self.save_data_option, text='Close',
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.winclose)
        self.data_cancel.grid(row=2, column=1, padx=(0, 8), pady=(10, 0))


    def reset_entry(self):
        """This function is use to reset the entry box"""
        self.item_sales.delete(0, 20)
        self.quantity.delete(0, 20)
        self.price.delete(0, 20)
        self.amount_paid.delete(0, 20)
        self.balance_left.delete(0, 20)
        self.served_by.delete(0, 20)
        self.contact.delete(0, 20)


    def winclose(self) -> None:
        """This method exit the data_edit window when the button is press"""
        msg = CTkMessagebox(title='Close window', message='Do you want to exit?\
                                Remember to save your data', 
                                option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.userdata.destroy()
        else:
            return 


    def send_request(self):
        """This method is to get data from user entry and insert it into the database"""
        try:
            its = str(self.item_sales.get()).upper()
            itq = int(self.quantity.get())
            itp = int(self.price.get())
            amt = int(self.amount_paid.get())
            bl = self.balance_left.get()
            svb = str(self.served_by.get()).upper()
            ct = int(self.contact.get())
            dt = str(self.date)

            if its and itq and itp and amt and svb and ct and dt:
                if not bl or bl == 0:
                    bl = "-"
                try:
                    database.insert_daily_sales(its, itq, itp, amt, bl, svb, ct, dt)
                    CTkMessagebox(title='Successful', message='Data saved successfully',
                                  icon='check', option_1='Ok')

                except:
                    CTkMessagebox(title='Error',
                                  message="Can't add data to the database. Please check the ID",
                                  icon='cancel', option_1='Ok')
            else:
                CTkMessagebox(title='Warning',
                              message="Empty field is not allowed!",
                              option_1='Try again', icon='warning')
        except ValueError:
            CTkMessagebox(title='Error',
                          message="Please enter a valid number",
                          icon='cancel', option_1='Ok')


