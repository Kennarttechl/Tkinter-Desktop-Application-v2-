"""This are built-in modules, which are part of the Python Standard Library"""
import sys
import json
import tkinter
import sqlite3
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import Menu
from threading import Timer

"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox

"""These are local modules that I have created myself and are part of the project"""
from daily__sales.user_data import UserData
import user__dashboard.newframes as newframes
from data_table.result_table import ResultTable
from app_database.database import resource_path
from app_image_utils.image_utils import get_ctk_image
from app_database.export_data import export_data_exceld


class Dashboard(customtkinter.CTkToplevel):

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open the a json file"""
    with open(file='config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)

    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.minsize(1000, 510)
        self.geometry('1000x550+135+50')
        self.title('Welcome to DS Enterprise')
        self.after(1, lambda: self.state("zoomed"))
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.columnconfigure((1,2), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        self.date = datetime.datetime.now().date()

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
                                     accelerator='Ctrl+I', command=self.get_data)

        self.left_frame = customtkinter.CTkFrame(master=self, border_color='gray25', 
                                            border_width=0.8, corner_radius=8,
                                            fg_color='#595959')
        self.left_frame.grid(row=0, column=0, padx=(6, 40), pady=(8, 8), sticky=NSEW)
        self.left_frame.grid_rowconfigure(0, weight=1)

        self.user_profile = customtkinter.CTkLabel(master=self.left_frame, text_color='#F29F05',
                                                   text='\n\n\n\n\n\nWelcome to \nDaily Sales',
                                              image=get_ctk_image(icon='logo_05', size=80),
                                              font=customtkinter.CTkFont('Roboto', 16))
        self.user_profile.grid(row=0, column=0, padx=(7, 20), pady=(0, 20), sticky=NSEW)

        self.new_frame_button = customtkinter.CTkButton(master=self.left_frame,
                                                        text='New Frames',
                                                        text_color=("gray10", "gray90"), 
                                                        fg_color=("gray70", "gray26"),
                                                        hover_color='#3B8C66', height=25, width=18, anchor='w',corner_radius=5,
                                                        image=get_ctk_image(icon='photo-frame',
                                                                       size=19),
                                                        command=self.new_frame_dashbord)
        self.new_frame_button.grid(row=1, column=0, padx=(15, 15), pady=(0, 150), sticky=EW)


        self.daily_sales_button = customtkinter.CTkButton(master=self.left_frame,
                                                          text='Export Data',
                                                          text_color=("gray10", "gray90"),hover_color=("gray70", "gray26"), height=25, width=18, anchor='w',
                                                          fg_color='#3B8C66', corner_radius=5,image=get_ctk_image(icon='excel', size=19), command=self.save_data)
        self.daily_sales_button.grid(row=1, column=0, padx=(15, 15), pady=(0, 50), sticky=EW)


        self.log__home = customtkinter.CTkButton(master=self.left_frame, height=24,
                                                 text='Logout',
                                                 text_color=("gray10", "gray90"),
                                                 fg_color=("gray70", "gray26"),
                                                 hover_color='#3B8C66',
                                                 corner_radius=5, anchor='w', width=18,
                                                 image=get_ctk_image(icon='logout', size=19),
                                                 command=self.logout_home)
        self.log__home.grid(row=4, column=0, padx=(15, 15), pady=(100, 100), sticky=EW)


        self.middle_frame = customtkinter.CTkFrame(master=self, border_width=1,height=100,
                                                   border_color='gray40', width=1320, 
                                                   corner_radius=6, )
        self.middle_frame.grid(row=0, column=1, columnspan=4, padx=(0, 10), pady=(10, 10), 
                               sticky=NSEW)
        self.middle_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.middle_frame.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)


        """----------------------Columns and Table-------------------------"""
        self.style = ttk.Style(master=self)
        self.style.theme_use('clam')

        font = ("Cascadia Mono", 11, 'bold')

        self.style.configure('Treeview', background="gray28", foreground='white', 
                             rowheight=30, fieldbackground="#3D3D3D", font=font)
        
        self.style.map('Treeview', background=[('selected', 'gray30')])

        self.tree = ttk.Treeview(master=self.middle_frame,
                                 columns=("col1", "col2", "col3"), show='headings')
        
        self.tree.tag_configure('evenrow', background="#173540")
        self.tree.tag_configure('oddrow', background="#16232E")
        

        self.tree['columns'] = ('item sold', 'quantity', 'price', 'amount', 
                                'balance', 'served by', 'contact','date')
        
        # self.tree.heading('rowid', text='Rowid')
        self.tree.heading('item sold', text='Item Sold')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('price', text='Price')
        self.tree.heading('amount', text='Amount')
        self.tree.heading('balance', text='Balance')
        self.tree.heading('served by', text='Served By')
        self.tree.heading('contact', text='Contact')
        self.tree.heading('date', text='Date')

        # self.tree.column("rowid", width=200)
        self.tree.column("item sold", width=100, anchor='center')
        self.tree.column("quantity", width=100, anchor='center')
        self.tree.column("price", width=100, anchor='center')
        self.tree.column("amount", width=100, anchor='center')
        self.tree.column("balance", width=100, anchor='center')
        self.tree.column("served by", width=100, anchor='center')
        self.tree.column("contact", width=100, anchor='center')
        self.tree.column("date", width=100, anchor='center')
        self.tree.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_all_record()

        self.vsb = customtkinter.CTkScrollbar(master=self.middle_frame, orientation='vertical',
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, rowspan=6, column=8, pady=(40), sticky="ns")
        # self.vsb.pack(side='right', fill='y')
        # self.vsb.grid(row=1, column=4, sticky=N+S)

        self.hsb = customtkinter.CTkScrollbar(master=self.middle_frame, orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.grid(row=11, columnspan=6, column=0, sticky=E+W)
        # self.hsb.pack(side='bottom', fill='x')

        self.tree.grid(row=1, column=0, rowspan=10, columnspan=6, sticky='nsew')
        # self.tree.pack(expand=True, fill='both')

        self.top_frame = customtkinter.CTkFrame(master=self.middle_frame, border_color='gray50',
                                                border_width=0.4, width=400, height=40,corner_radius=4, fg_color='gray35')
        self.top_frame.grid(row=0, column=0, columnspan=6, padx=(2,2), pady=(2, 0), 
                       ipady=3, sticky='ew')
        self.top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        self.data_entry = customtkinter.CTkButton(master=self.top_frame, text='Daily Sales',
                                              width=80, height=24, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.mydata)
        self.data_entry.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))

        self.quantity_entry = customtkinter.CTkButton(master=self.top_frame,
                                                      text='Refresh table',
                                                      width=80, height=24, corner_radius=4,
                                                      hover_color=('gray70', 'gray30'),
                                                      command=self.table_refresh)
        self.quantity_entry.grid(row=0, column=1, padx=(0, 0), pady=(3, 0))

        self.search_box = customtkinter.CTkEntry(master=self.top_frame, height=30,
                                                 placeholder_text='Search for item....',
                                                 width=220, corner_radius=7, border_width=2,)
        self.search_box.grid(row=0, column=3, padx=(0, 120), pady=(3, 0))

        self.search_button = customtkinter.CTkButton(master=self.top_frame, text='',
                                                     width=38, height=24, corner_radius=5,
                                                     font=customtkinter.CTkFont('Sans', 13),
                                                     hover_color=('gray70', 'gray30'),
                                                     fg_color='gray15',
                                                     image=get_ctk_image(icon='logo_08', size=20),
                                                     compound='left', command=self.data_search,
                                                     border_color='gray40',border_width=1,)
        self.search_button.grid(row=0, column=3, padx=(70, 0), pady=(3, 0))

        # self.logout_timer = None # Timer for auto-logout
        # self.start_logout_timer() # Start the logout timer

        self.bind('<Control-i>', self.get_data)
        self.bind('<Control-I>', self.get_data)

        #Note value formating = "${0:.2f}".format(value)

    def start_logout_timer(self):
        if self.logout_timer is not None:
            self.logout_timer.cancel()
        
        timeout_duration = 60  # 2 minutes

        # Start the timer
        self.logout_timer = Timer(timeout_duration, self.logout)
        self.logout_timer.start()

        self.bind("<Key>", self.reset_timer)  # Bind key events to reset the timer
        self.bind("<Button>", self.reset_timer)  # Bind mouse events to reset the timer

    def reset_timer(self, event=None):
        self.start_logout_timer()

    def logout(self):
        pass
        # self.withdraw()
        # self.parent.deiconify()
        # self.logout_timer = None

    def mydata(self):
        UserData(self)

    def get_data(self, *args):
        ResultTable()

    def save_data(self):
        export_data_exceld()

    def get_cursor(self, *event):
        cursor_row = self.tree.focus()
        contents = self.tree.item(cursor_row)
        row = contents['values']

    def logout_home(self):
        msg = CTkMessagebox(title='Logout', message='Do you want to logout',
                            option_1='Yes', option_2='No', icon='info')
        if msg.get() == 'Yes':   
            self.parent.deiconify()
            self.destroy()
        else:
            return
        
    def on_close(self):
        msg = CTkMessagebox(title='Exit', message='Are you sure you want to exit',
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            sys.exit()
        else:
            return

    def new_frame_dashbord(self):
        newframes.Newframe(self)
        self.withdraw()
        self.iconify()
        self.withdraw()

    def show_all_record(self) -> None:
        try:
            connection = sqlite3.connect(resource_path('data__/daily_database.db'))
            conn = connection.cursor()
            conn.execute("SELECT * FROM data_collection")
            rows = conn.fetchall()
            if len(rows) != 0:
                self.tree.delete(*self.tree.get_children())
                for index, row in enumerate(rows):
                    if index % 2 == 0:# Use 'index' instead of 'row' for modulus operation
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

    def data_search(self):
        try:
            value = self.search_box.get().lower()
            connection = sqlite3.connect(resource_path("data__/daily_database.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM data_collection WHERE item_sales LIKE ?",
                         ('%'+value+'%',))
            rows = conn.fetchall()
            if len(rows) != 0:
                CTkMessagebox(title='Found', message='Record found',
                              icon='check', option_1='Ok')
                self.tree.delete(*self.tree.get_children())
                for index, row in enumerate(rows):
                    if index % 2 == 0:
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

    def table_refresh(self):
        try:
            value = self.search_box.get().lower()
            connection = sqlite3.connect(resource_path("data__/daily_database.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM data_collection WHERE item_sales LIKE ?",
                         ('%'+value+'%',))
            rows = conn.fetchall()
            if len(rows) != 0:
                pass
                self.tree.delete(*self.tree.get_children())
                for index, row in enumerate(rows):
                    if index % 2 == 0:
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


# def Main_d():
#     load = customtkinter.CTk()
#     load = Dashboard()
#     load.title('Dashboad')
#     load.mainloop()

# if __name__ == "__main__":
#     app = Main_d()
    
    