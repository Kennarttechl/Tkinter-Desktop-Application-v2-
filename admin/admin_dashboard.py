"""This are built-in modules, which are part of the Python Standard Library"""
import sys
import json
import threading
from tkinter import *
from tkinter import Menu
from threading import Timer
from datetime import datetime

"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox

"""This are local modules created by me and are part of the project"""
import app_about.about as about
from fetch.data_display import load_data
import super_entry.customnote as customnote
from user_logins.register import UserSignup
from super_entry.admin_entry import NewEntry
import user__dashboard.newframes as newframes
from slides.animated_window import SlidePanel
import user__dashboard.dashboard as dashboard
from data_modification.edit__data import EditData
from data_table.note_table_admin import NoteTable
from app_image_utils.image_utils import get_ctk_image
from data_table.result_table_admin import ResultTableA
from app_database.export_data import export_data_excela


class Adminsuper(customtkinter.CTkToplevel):
    """This class defines the Admin page, which is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme("green")

    with open(file='config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.withdraw()
        self.minsize(850, 450)
        self.geometry('1000x515+125+60')
        self.title('Welcome to DS Enterprise')
        self.after(1, lambda: self.state('zoomed'))
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.slide_panel = None
        self.logout_timer = None  # Timer for auto-logout

        self.columnconfigure((1,2), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        self.date = datetime.now().date()

        self.menu = Menu(self)
        self.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, 
                             activebackground='gray20', activeforeground='white')
        self.menu.add_cascade(label='File', menu=self.filename)
        self.filename.add_command(label='Exit       ', accelerator='Ctrl+Q', 
                                  command=self.on_close)

        self.help = Menu(self.menu, tearoff=0, activebackground='gray20',
                         activeforeground='white', activeborderwidth=0)
        self.menu.add_cascade(label='Help', menu = self.help)
        self.help.add_command(label='About      ', accelerator='Ctrl+A', 
                              command=self.about)

        self.option_menu = Menu(self.menu, tearoff=0, activebackground='gray20', 
                                activeforeground='white')
        self.menu.add_cascade(label='Options', menu = self.option_menu)
        # self.option_menu.add_command(label='Print       ', 
        #                              accelerator='Ctrl+P', command=None)
        self.option_menu.add_command(label='View All Data', 
                                     accelerator='Ctrl+I', command=self.get_data)
        self.option_menu.add_command(label='View Note Data', 
                                     accelerator='Ctrl+N', command=self.get_note_data)


        self.left_frame = customtkinter.CTkFrame(master=self, border_color='gray25',
                                                 border_width=0.8, corner_radius=8,fg_color='#595959')
        self.left_frame.grid(row=0, column=0, padx=(6, 40), pady=(8, 8), sticky=NSEW)
        self.left_frame.grid_rowconfigure(0, weight=1)


        self.user_profile = customtkinter.CTkLabel(master=self.left_frame, text_color='#F29F05',
                                                   text='\n\n\n\n\n\nWelcome to \nAdmin Dashboard',image=get_ctk_image(icon='logo_05', size=80),font=customtkinter.CTkFont('Roboto', 16))
        self.user_profile.grid(row=0, column=0, padx=(7, 20), pady=1, sticky=NSEW)


        self.new_frame_button = customtkinter.CTkButton(master=self.left_frame,
                                                        text='New Frames', corner_radius=5,
                                                        text_color=("gray10", "gray90"), 
                                                        fg_color=("gray70", "gray26"),
                                                        height=20, width=25, anchor='w', hover_color='#3B8C66',
                                                        image=get_ctk_image(icon='logo_10', size=19),
                                                        command=self.gotonewf)
        self.new_frame_button.grid(row=2, column=0, padx=(15, 20), pady=(1, 20), sticky=EW)


        self.daily_sales_button = customtkinter.CTkButton(master=self.left_frame, 
                                                          height=25,text='Dashboard',
                                                          text_color=("gray10", "gray90"),width=25, 
                                                          fg_color=("gray70", "gray26"),hover_color='#3B8C66',
                                                          corner_radius=5, anchor='w', 
                                                          image=get_ctk_image(icon='dashboard', size=19), 
                                                          command=self.user_dashboard)
        self.daily_sales_button.grid(row=3, column=0, padx=(15, 20), pady=(0, 20), sticky=EW)


        self.create_new_user = customtkinter.CTkButton(master=self.left_frame, height=25,
                                                       text='New User',
                                                       fg_color=("gray70", "gray26"),
                                                       hover_color='#3B8C66',
                                                       text_color=("gray10", "gray90"),
                                                       corner_radius=5, anchor='w', width=25,
                                                       image=get_ctk_image(icon='userss', size=19),
                                                       command=self.new_user)
        self.create_new_user.grid(row=4, column=0,  padx=(15, 20), pady=(0, 250), sticky=EW)


        self.create_new_user = customtkinter.CTkButton(master=self.left_frame, height=25,
                                                       text='More Options',
                                                       text_color=("gray10", "gray90"),
                                                       fg_color=("gray70", "gray26"),
                                                       hover_color='#3B8C66',
                                                       corner_radius=5, anchor='w', width=25,
                                                       image=get_ctk_image(icon='application', size=19),
                                                       command=self.animated_panel)
        self.create_new_user.grid(row=4, column=0,  padx=(15, 20), pady=(0, 150), sticky=EW)


        self.log__home = customtkinter.CTkButton(master=self.left_frame, height=25,
                                                 text='Logout',
                                                 text_color=("gray10", "gray90"),
                                                 fg_color=("gray70", "gray26"),
                                                 hover_color='#3B8C66',
                                                 corner_radius=5, anchor='w', width=25,
                                                 image=get_ctk_image(icon='logout', size=19), 
                                                 command=self.home_logout)
        self.log__home.grid(row=4, column=0, padx=(15, 20), pady=(130, 0), sticky=EW)


        self.middle_frame = customtkinter.CTkFrame(master=self, border_width=1,
                                                   border_color='gray40',
                                                   corner_radius=6, width=1320, height=100)
        self.middle_frame.grid(row=0, column=1, columnspan=2, padx=(0,10), pady=(10, 10), 
                               sticky=NSEW)
        
        self.middle_frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.middle_frame.grid_rowconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)


        self.top_frame = customtkinter.CTkFrame(master=self.middle_frame, corner_radius=4, 
                                                border_width=0.6, width=400, height=40,
                                                border_color='gray50', fg_color='gray35')
        self.top_frame.grid(row=0, column=0, columnspan=4, padx=(2, 2), pady=(2, 0),
                            ipady=3, sticky='ew')
        

        self.top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8,10,12), weight=1)

        """---------------------Data Collection frames----------------------"""
        self.item_mug = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#28403D', corner_radius=6)
        self.item_mug.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky='nswe')
        self.display_data_on_labels()


        self.a4frame = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#889C9B', corner_radius=6)
        self.a4frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky='nswe')


        self.a3frame = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#6C786B', corner_radius=6)
        self.a3frame.grid(row=1, column=2, padx=(20, 20), pady=(20, 20), sticky='nswe')


        self.a5frame = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#A6A48D', corner_radius=6)
        self.a5frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 20), sticky='nswe')


        self.a2frame = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#D1CCAF', corner_radius=6)
        self.a2frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 20), sticky='nswe')


        self.a4local = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#0367A6', corner_radius=6)
        self.a4local.grid(row=2, column=1, padx=(20, 20), pady=(10, 20), sticky='nswe')


        self.a3local = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#D95E32', corner_radius=6)
        self.a3local.grid(row=2, column=2, padx=(20, 20), pady=(10, 20), sticky='nswe')


        self.a3foreign = customtkinter.CTkFrame(master=self.middle_frame, height=180, 
                                               width=60, fg_color='#F2B84B', corner_radius=6)
        self.a3foreign.grid(row=2, column=3, padx=(20, 20), pady=(10, 20), sticky='nswe')
        """------------------------Data Collection Frames-------------------"""


        self.data_modify = customtkinter.CTkButton(master=self.top_frame, text='Daily Sales',
                                                   width=80, height=24, corner_radius=4,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.dataentry)
        self.data_modify.grid(row=0, column=0, padx=(6, 0), pady=(5, 0))


        self.txt_note = customtkinter.CTkButton(master=self.top_frame, width=80,
                                                text='New Note',
                                                hover_color=('gray70', 'gray30'),
                                                font=('Sans', 13), height=24,
                                                corner_radius=4, command=self.adminnote)
        self.txt_note.grid(row=0, column=1, padx=(0,140), pady=(5,0))


        self.data_modify = customtkinter.CTkButton(master=self.top_frame,
                                                   text='Modify Data',
                                                   width=80, height=24, corner_radius=4,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.modify_dt)
        self.data_modify.grid(row=0, column=1, padx=(100, 0), pady=(5, 0))

        """End of the frames"""
        self.buttom_frame = customtkinter.CTkFrame(master=self.middle_frame, corner_radius=3,
                                                   border_width=0.4, width=400, height=40,
                                                   border_color='gray50')
        self.buttom_frame.grid(row=11, column=0, columnspan=4, padx=(2, 2), pady=(0, 1),
                            ipady=2, sticky='ew')
        self.buttom_frame.grid_columnconfigure((0,1,2), weight=1)


        self.print_data = customtkinter.CTkButton(master=self.buttom_frame, width=80,
                                                   text_color=("white"), height=25,
                                                   fg_color=self.user_data['theme3'],
                                                   hover_color=("gray70", "gray30"),
                                                   anchor='S',text='Print Data',
                                                   corner_radius=4,
                                                   font=('Roboto', 13),command=None)
        self.print_data.grid(row=5, column=6, padx=(0, 120), pady=(3, 0), sticky='e')


        self.submit_button = customtkinter.CTkButton(master=self.buttom_frame,
                                                     text='Export Data', compound='left',
                                                     image=get_ctk_image(icon='excel', size=19),
                                                     text_color=("white"), corner_radius=4,
                                                     fg_color='#3B8C66', font=('Roboto', 13),
                                                     hover_color=("gray70", "gray26"),
                                                     height=18, width=76, anchor='S',
                                                     command=self.datasave)
        self.submit_button.grid(row=5, column=6, padx=(20, 6), pady=(3, 0), sticky='e')


        self.display_calendar = customtkinter.CTkLabel(master=self.buttom_frame,
                                                       text="Today's date " + str(self.date),
                                                       font=('Sans', 12),)
        self.display_calendar.grid(row=5, column=1, padx=(5, 0), pady=(4, 2))

        
        """This are 'Shortcut' keys"""
        self.bind('<Control-a>', self.about)
        self.bind('<Control-A>', self.about)
        self.bind('<Control-i>', self.get_data)
        self.bind('<Control-I>', self.get_data)
        self.bind('<Control-N>', self.get_note_data)
        self.bind('<Control-n>', self.get_note_data)


    def display_data_on_labels(self):
        serialized_data = load_data()
        if serialized_data is not None:
            for index, data in enumerate(serialized_data):
                row_offset = index * 6  # Adjust the row offset based on the index
                for col_index, (key, value) in enumerate(data.items()):
                    display_label = customtkinter.CTkLabel(master=self.item_mug, 
                                                           text_color='#CACACA',
                                                           font=('MusticaPro-SemiBold', 15),
                                                           text=f'{key}: {value}')
                    display_label.grid(row=row_offset + col_index, column=0,
                                    padx=(4, 0), pady=(0, 0), sticky='w')
                    

    def on_close(self):
        sys.exit()


    # def log(self):
    #     start_logout_timer() # Start the logout timer

    # def start_logout_timer(self):
    #     if self.logout_timer is not None:
    #         self.logout_timer.cancel()
        
    #     timeout_duration = 120  # 2 minutes

    #     # Start the timer
    #     self.logout_timer = Timer(timeout_duration, self.logout)
    #     self.logout_timer.start()

        self.bind("<Key>", self.reset_timer)  # Bind key events to reset the timer
        self.bind("<Button-1>", self.reset_timer)  # Bind mouse events to reset the timer
        self.bind("<Button-2>", self.reset_timer)  # Bind mouse events to reset the timer
        self.bind("<Button-3>", self.reset_timer)  # Bind mouse events to reset the timer

    # def reset_timer(self, event=None):
    #     print('Resetting time')
    #     self.start_logout_timer()

    # def logout(self):
    #     pass
    #     self.withdraw()
    #     self.root.deiconify()
    #     self.logout_timer = None

    def gotonewf(self):
        newframes.Newframe(self)
        self.withdraw()
        self.iconify()
        self.withdraw()
        
    def user_dashboard(self):
        dashboard.Dashboard(self)
        self.withdraw()
        self.iconify()
        self.withdraw()

    def get_note_data(self, *event):
        NoteTable()

    def dataentry(self):
        NewEntry(self)

    def datasave(self):
        export_data_excela()

    def new_user(self):
        UserSignup(self)

    def get_data(self, *args):
        ResultTableA()
    
    def modify_dt(self):
        EditData(self)

    def about(self, *args):
        about.about_(self)

    def adminnote(self):
        customnote.CustomNote(self)

    def animated_panel(self):
        if self.slide_panel is None:
            self.slide_panel = SlidePanel(self.middle_frame, 1.0, 0.10)
        self.slide_panel.animate()

    def home_logout(self):
        self.root.deiconify()
        self.destroy()  

    
# def Main_a():
#     mm = customtkinter.CTk()
#     mm = Adminsuper()
#     mm.title('Admin-Dashboard')
#     mm.mainloop()


# if __name__ == "__main__":
#     app = Main_a()
#     admin_dashboard = Adminsuper(app.root)
