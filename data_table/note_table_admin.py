"""This are built-in modules, which are part of the Python Standard Library"""
import sqlite3
import tkinter
from tkinter import NSEW
from tkinter import END, ttk
from tkinter import LEFT, Menu  #import tkinter's Image class as TkImage

"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from app_database.database import resource_path
from app_image_utils.image_utils import get_ctk_image
from CTkMessagebox import CTkMessagebox


class NoteTable():

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')
    
    def __init__(self) -> None:
        # self.master_window = customtkinter.CTk()
        self.master_window = customtkinter.CTkToplevel()
        self.master_window.title('Admin Data Table')
        self.master_window.geometry('1100x550+110+60')
        self.master_window.attributes('-topmost', True)
        self.master_window.withdraw()
        self.master_window.after(500, self.master_window.deiconify)

        self.master_window.columnconfigure(0, weight=1, uniform='a')
        self.master_window.rowconfigure(1, weight=1, uniform='a')

        self.menu = Menu(self.master_window)
        self.master_window.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, 
                             activebackground='gray20', activeforeground='white')
        self.menu.add_cascade(label='File', menu=self.filename)
        self.filename.add_command(label='Exit      ', accelerator='Ctrl+Q', command=self.exitt)


        self.top_frame = customtkinter.CTkFrame(master=self.master_window, 
                                                fg_color='gray35', height=45, 
                                                corner_radius=3, bg_color='#2C3333')
        self.top_frame.grid(row=0, column=0, pady=(0, 0), sticky='nsew')
        self.top_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')


        self.search_box = customtkinter.CTkEntry(master=self.top_frame,
                                                 placeholder_text='Search for item....',
                                                 corner_radius=8, width=240, height=30)
        self.search_box.grid(row=0, column=2, padx=(0, 25), pady=(6, 6))

        
        self.search_button = customtkinter.CTkButton(master=self.top_frame, text='',
                                                     width=60, height=27, corner_radius=5,
                                                     font=('Sans', 13),
                                                     hover_color=('gray70', 'gray30'),
                                                     fg_color='gray15', compound='left', 
                                                     border_color='gray40', border_width=1, 
                                                     image=get_ctk_image(icon="logo_08",size=20),
                                                     command=self.data_search)
        self.search_button.grid(row=0, column=2, padx=(145, 0), pady=(6, 6))


        self.middle_frame = customtkinter.CTkFrame(master=self.master_window, 
                                                   fg_color='#20262E',)
        self.middle_frame.grid(row=1, column=0, rowspan=4, pady=(1, 1), sticky=NSEW)
        

        self.style = ttk.Style(master=self.master_window)
        self.style.theme_use('clam')

        self.font = ("Cascadia Mono", 11, 'bold')

        self.style.configure('Treeview', background="gray28", foreground='white', 
                             rowheight=30, fieldbackground="#3D3D3D", font=self.font)
        
        self.style.map('Treeview', background=[('selected', 'gray30')])


        self.tree = ttk.Treeview(master=self.middle_frame, 
                                 columns=("col1", "col2", "col3"),show='headings')
        
        self.tree.tag_configure('evenrow', background="#173540")
        self.tree.tag_configure('oddrow', background="#16232E")

        
        self.tree['columns'] = ('title', 'contents')
        
        self.tree.heading("title", text='Note title')
        self.tree.heading("contents", text='Note Contents')

        self.tree.column("title", width=100, anchor='center')
        self.tree.column("contents", width=300, anchor='center')
        self.show_all_records()

            
        self.vsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='vertical', 
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side='right', fill='y')


        self.hsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.pack(side='bottom', fill='x')

        self.tree.pack(expand=True, fill='both')


        self.master_window.bind('<Control-q>', self.exitt)
        self.master_window.bind('<Control-Q>', self.exitt)

        # self.master_window.mainloop()

    def exitt(self, *args):
        self.master_window.destroy()
        
    def print_data(self, *event)-> None:
        pass

    def data_search(self):
        try:
            value = self.search_box.get().lower()
            connection = sqlite3.connect(resource_path("data__/ds_note.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM admin_note WHERE note_title LIKE ?",
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
            CTkMessagebox(title='Error',
                          message='There was a problem with the\
                            Database!! Contact your system Admin',
                            icon='cancel', option_1='Try again')
        finally:
            connection.close()

            
    def show_all_records(self):
        try:
            connection = sqlite3.connect(resource_path("data__/ds_note.db"))
            conn = connection.cursor()
            conn.execute(" SELECT * FROM admin_note")
            rows = conn.fetchall()
            for index, row in enumerate(rows):
                if index % 2 == 0:# Use 'index' instead of 'row' for modulus operation
                    self.tree.insert('', tkinter.END, values=row, tags=("evenrow",))
                else:
                    self.tree.insert('', tkinter.END, values=row, tags=("oddrow",))
                connection.commit()
            connection.close()
        except sqlite3.Error as a:
            CTkMessagebox(title='Error',
                          message=f'There is a problem displaying the data {a}',
                          option_1='Ok', icon='cancel')


# if __name__ == "__main__":
#     app = NoteTable()
