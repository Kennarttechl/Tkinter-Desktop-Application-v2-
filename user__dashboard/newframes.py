"""This are built-in modules, which are part of the Python Standard Library"""
import sys
import json
import sqlite3
import tkinter
from tkinter import *
from threading import Timer

"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from tkinter import ttk
from CTkMessagebox import CTkMessagebox

"""These are local modules that I have created myself and are part of the project"""
import user__dashboard.dashboard as dashboard
from app_database.database import resource_path
from daily__sales.new_frame_entry import Userdata2
from app_image_utils.image_utils import get_ctk_image
from data_table.result_table_stock import ResultTableF
from app_database.export_data import export_data_excels


class Newframe(customtkinter.CTkToplevel):
    """This class defines the Newframe page, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open or load the a json file"""
    with open(file='config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)

    def __init__(self, root, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.root = root
        self.minsize(1000, 510)
        self.geometry('1000x550+135+50')
        self.title('Welcome to DS Enterprise')
        self.after(1, lambda: self.state("zoomed"))
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.columnconfigure((1,2), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        
        self.menu = Menu(self)
        self.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, activebackground=self.user_data
                             ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label='File', menu = self.filename)
        self.filename.add_command(label = 'Save', accelerator = 'Ctrl+S', command=None)

        self.option_menu = Menu(self.menu, tearoff=0, activebackground=self.user_data
                                ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label = "Options", menu = self.option_menu)

        self.option_menu.add_command(label = 'View All Data', 
                                     accelerator='Ctrl+I', command=self.view_data)

        self.left_frame = customtkinter.CTkFrame(master=self, border_color='gray25', 
                                            border_width=0.8, corner_radius=8,
                                            fg_color='#595959')
        self.left_frame.grid(row=0, column=0, padx=(6, 40), pady=(8, 8), sticky=NSEW)
        self.left_frame.grid_rowconfigure(0, weight=1)

        self.user_profile = customtkinter.CTkLabel(master=self.left_frame, text_color='#F29F05',
                                                   text='\n\n\n\n\n\nWelcome to \nNew Stock',
                                              image=get_ctk_image(icon='logo_05', size=80),
                                              font=customtkinter.CTkFont('Roboto', 16))
        self.user_profile.grid(row=0, column=0, padx=(7, 20), pady=(0, 20), sticky=NSEW)


        self.daily_sales_button = customtkinter.CTkButton(master=self.left_frame,
                                                          text='Daily Sales',
                                                          text_color=("gray10", "gray90"), fg_color=("gray70", "gray26"),hover_color='#3B8C66',
                                                          height=25, width=18, anchor='w',corner_radius=5, image=get_ctk_image(icon='stock-market',size=19), command=self.Dsales)
        self.daily_sales_button.grid(row=1, column=0, padx=(15, 15), pady=(0, 150), sticky=EW)


        self.daily_sales_button = customtkinter.CTkButton(master=self.left_frame, 
                                                          text='Export Data',
                                                          text_color=("gray10", "gray90"),hover_color=("gray70", "gray26"), height=25, width=18,
                                                          corner_radius=5, anchor='w',
                                                          fg_color='#3B8C66', image=get_ctk_image(icon='excel', size=19), 
                                                          command=self.save_export)
        self.daily_sales_button.grid(row=1, column=0, padx=(15, 15), pady=(0, 50), sticky=EW)


        self.log__home = customtkinter.CTkButton(master=self.left_frame, height=25,
                                                 text='Logout',
                                                 text_color=("gray10", "gray90"),
                                                 fg_color=("gray70", "gray26"),hover_color='#3B8C66',
                                                 corner_radius=5, anchor='w', width=18,image=get_ctk_image(icon='logout', size=19), command=self.back_home)
        self.log__home.grid(row=4, column=0, padx=(15, 15), pady=(100, 100), sticky=EW)


        self.middle_frame = customtkinter.CTkFrame(master=self, border_width=1,height=100,
                                                   border_color='gray40', width=1320, 
                                                   corner_radius=6, )
        self.middle_frame.grid(row=0, column=1, columnspan=4, padx=(0, 10), pady=(10, 10), 
                               sticky=NSEW)
        self.middle_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.middle_frame.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        

        self.style = ttk.Style(master=self)
        self.style.theme_use('clam')

        self.font = ('Cascadia Mono', 11, 'bold')


        self.style.configure('Treeview', background="gray28", foreground='white', 
                             rowheight=30, fieldbackground="#3D3D3D", font=self.font)
        

        self.style.map('Treeview', background=[('selected', 'gray30')])
        

        self.tree = ttk.Treeview(master=self.middle_frame,
                                 columns=("col1", "col2", "col3"), show='headings')
        
        self.tree.tag_configure('evenrow', background="#173540")
        self.tree.tag_configure('oddrow', background="#16232E")
        
        
        self.tree['columns'] = ('new item', 'quantity', 'price', 'date')
        
        self.tree.heading('new item', text='Item Name')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('price', text='Price')
        self.tree.heading('date', text='Date')

        # self.tree.column("id", width=200)
        self.tree.column("new item", width=200, anchor='center')
        self.tree.column("quantity", width=200, anchor='center')
        self.tree.column("price", width=200, anchor='center')
        self.tree.column("date", width=200, anchor='center')
        self.show_all_record2()


        self.vsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                              button_hover_color='#FF0303', 
                                              orientation='vertical', 
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        # self.vsb.pack(side='right', fill='y')
        # self.vsb.grid(row=1, column=4, sticky=N+S)

        self.hsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                              orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.grid(row=11, columnspan=6, column=0, sticky=E+W)
        # self.hsb.pack(side='bottom', fill='x')

        self.tree.grid(row=1, column=0, rowspan=10, columnspan=6, sticky='nsew')
        # self.tree.pack(expand=True, fill='both')
        # self.tree.grid(row=1, column=0, rowspan=7, columnspan=4, sticky='nsew')
        """----------------------Columns and Table-------------------------"""
        # self.hsb.pack(side='bottom', fill='x')


        self.top_frame = customtkinter.CTkFrame(master=self.middle_frame, border_color='gray50',
                                                border_width=0.4, width=400, height=40,fg_color='gray35', corner_radius=4)
        self.top_frame.grid(row=0, column=0, columnspan=6, padx=(2,2), pady=(2, 0), ipady=3, 
                            sticky='ew')
        self.top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)


        self.data_entry = customtkinter.CTkButton(master=self.top_frame, text='Enter Data',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.new_entry_data)
        self.data_entry.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))
        

        self.tbl_refresh = customtkinter.CTkButton(master=self.top_frame, text='Refresh table',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.tabel_refresh)
        self.tbl_refresh.grid(row=0, column=1, padx=(0, 0), pady=(3, 0))


        self.search_entry = customtkinter.CTkEntry(master=self.top_frame, height=30,
                                                 placeholder_text='Search for item....',
                                                 width=220, corner_radius=7, border_width=2,)
        self.search_entry.grid(row=0, column=3, padx=(0, 120), pady=(3, 0))

        
        self.search_button = customtkinter.CTkButton(master=self.top_frame, text='',
                                                width=38, height=24, corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', 
                                                image=get_ctk_image(icon='logo_08', size=20),
                                                compound='left', command=self.data_search2,
                                                border_color='gray40',border_width=1,)
        self.search_button.grid(row=0, column=3, padx=(70, 0), pady=(3, 0))

        # self.logout_timer = None # Timer for auto-logout
        # self.start_logout_timer() # Start the logout timer

        self.bind('<Control-i>', self.view_data)
        self.bind('<Control-I>', self.view_data)

    def on_close(self):
        sys.exit()

    def start_logout_timer(self):
        if self.logout_timer is not None:
            self.logout_timer.cancel()
        
        timeout_duration = 120  # 2 minutes

        # Start the timer
        self.logout_timer = Timer(timeout_duration, self.logout)
        self.logout_timer.start()

        self.bind("<Key>", self.reset_timer)  # Bind key events to reset the timer
        self.bind("<Button>", self.reset_timer)  # Bind mouse events to reset the timer

    def reset_timer(self, event=None):
        self.start_logout_timer()

    def logout(self):
        pass
        # self.root.deiconify()
        # self.destroy()  # Close the admin dashboard window
        # self.logout_timer = None

    def save_export(self):
        export_data_excels()

    def new_entry_data(self):
        Userdata2(self)

    def view_data(self, *args):
        ResultTableF()

    def Dsales(self):
        dashboard.Dashboard(self)
        self.withdraw()
        self.iconify()
        self.withdraw()

    def back_home(self):
        self.root.deiconify()
        self.destroy()

    def show_all_record2(self) -> None:
        try:
            connection = sqlite3.connect(resource_path("data__/new_frame.db"))
            conn = connection.cursor()
            conn.execute(" SELECT * FROM ds_newframe")
            rows = conn.fetchall()
            for index, row in enumerate(rows):
                    if index % 2 == 0: # Use 'index' instead of 'row' for modulus operation
                        self.tree.insert('', tkinter.END, values=row, tags=("evenrow",))
                    else:
                        self.tree.insert('', tkinter.END, values=row, tags=("oddrow",))
                    connection.commit()
        except:
            CTkMessagebox(title='Error', message='There was a problem with the\
                            Database!! Contact your system Admin',
                            icon='cancel', option_1='Try again')
        finally:
            connection.close()


    def data_search2(self):
        try:
            value = self.search_entry.get().lower()
            connection = sqlite3.connect(resource_path("data__/new_frame.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM ds_newframe WHERE new_item LIKE ?",
                         ('%'+value+'%',))
            rows = conn.fetchall()
            if len(rows) != 0:
                CTkMessagebox(title='Found', message='Record found',
                              icon='check', option_1='Ok')
                self.tree.delete(*self.tree.get_children())
                for index, row in enumerate(rows):
                    if index % 2 == 0:  # Use 'index' instead of 'row' for modulus operation
                        self.tree.insert('', tkinter.END, values=row, tags=("evenrow",))
                    else:
                        self.tree.insert('', tkinter.END, values=row, tags=("oddrow",))
                    connection.commit()
            else:
                CTkMessagebox(title='No Record', message='Record not found',
                              icon='warning', option_1='try again')
        except:
             CTkMessagebox(title='Error', message='There was a problem with the\
                           Database!! Contact your system Admin',
                           icon='cancel', option_1='Try again')
        finally:
            connection.close()


    def tabel_refresh(self):
        try:
            value = self.search_entry.get().lower()
            connection = sqlite3.connect(resource_path("data__/new_frame.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM ds_newframe WHERE new_item LIKE ?",
                         ('%'+value+'%',))
            rows = conn.fetchall()
            if len(rows) != 0:
                pass
                self.tree.delete(*self.tree.get_children())
                for index, row in enumerate(rows):
                    if index % 2 == 0:  # Use 'index' instead of 'row' for modulus operation
                        self.tree.insert('', tkinter.END, values=row, tags=("evenrow",))
                    else:
                        self.tree.insert('', tkinter.END, values=row, tags=("oddrow",))
                    connection.commit()
            else:
                pass
        except:
             CTkMessagebox(title='Error', message='There was a problem with the\
                           Database!! Contact your system Admin',
                           icon='cancel', option_1='Try again')
        finally:
            connection.close()


# def Main_n():
#     load = customtkinter.CTk()
#     load = Newframe()
#     load.title('Welcome to DS Enterprise')
#     load.mainloop()


# if __name__ == "__main__":
#     app = Main_n()
