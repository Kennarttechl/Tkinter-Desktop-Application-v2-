"""This are built-in modules, which are part of the 
Python Standard Library"""
import sqlite3
import tkinter
from tkinter import ttk
from tkinter import NSEW
from tkinter import END, ttk
from tkinter import LEFT, Menu


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


class ResultTableF(customtkinter.CTkToplevel):

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.withdraw()
        self.title('New Stock')
        self.after(500, self.deiconify)
        self.geometry('1100x550+110+60')
        self.attributes('-topmost', True)

        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')

        self.menu = Menu(self)
        self.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, 
                             activebackground='gray20', activeforeground='white')
        self.menu.add_cascade(label='File', menu=self.filename)

        self.filename.add_command(label='Print Data     ', image=None, compound=LEFT, 
                                  accelerator='Ctrl+P', command=self.print_data)

        self.top_frame = customtkinter.CTkFrame(master=self, 
                                                fg_color='#2C3333', height=45, 
                                                corner_radius=2, bg_color='#2C3333')
        self.top_frame.grid(row=0, column=0, pady=(0, 0), ipady=3, sticky='nsew')
        self.top_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')

        self.middle_frame = customtkinter.CTkFrame(master=self, 
                                                   fg_color='#20262E',)
        self.middle_frame.grid(row=1, column=0, rowspan=4, pady=(1, 1), sticky=NSEW)

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
        
        # self.tree.heading('id', text='Id')
        self.tree.heading('new item', text='Item Name')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('price', text='Price')
        self.tree.heading('date', text='Date')

        # self.tree.column("id", width=200)
        self.tree.column("new item", width=200, anchor='center')
        self.tree.column("quantity", width=200, anchor='center')
        self.tree.column("price", width=200, anchor='center')
        self.tree.column("date", width=200, anchor='center')
        self.show_all_record()

        self.vsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                              orientation='vertical',
                                              button_hover_color='#16FF00', 
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side='right', fill='y')

        self.hsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                              orientation='horizontal',
                                              button_hover_color='#16FF00', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.pack(side='bottom', fill='x')

        self.tree.pack(expand=True, fill='both')

        self.bind('<Control-P>', self.print_data)
        self.bind('<Control-p>', self.print_data)


    def print_data(self, *event) -> None:
        pass

    def show_all_record(self) -> None:
        try:
            connection = sqlite3.connect("data__/new_frame.db")
            conn = connection.cursor()
            conn.execute(" SELECT * FROM ds_newframe")
            rows = conn.fetchall()
            for index, row in enumerate(rows):
                if index % 2 == 0:
                    self.tree.insert('', tkinter.END, values=row, tags=("evenrow",))
                else:
                    self.tree.insert('', tkinter.END, values=row, tags=("oddrow",))
                connection.commit()
            connection.close()
        except sqlite3.Error as a:
            CTkMessagebox(title='Error',
                          message=f'There is a problem displaying the data {a}',
                          option_1='Ok', icon='cancel')


# def Main_t():
#     load = customtkinter.CTk()
#     load = ResultTableF()
#     load.title('New Stock')
#     load.mainloop()

# if __name__ == "__main__":
#     app = Main_t()