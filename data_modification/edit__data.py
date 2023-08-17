"""This are built-in modules, which are part of the Python Standard Library"""
import json
import sqlite3
import tkinter
from tkinter import *

"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox

"""this are modules i create my self which are part of the project"""
import app_database.database as database
from app_database.database import resource_path
from app_image_utils.image_utils import get_ctk_image


class EditData():
    """This class defines the data_editpage that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using contex manager to open txt file for reading mode"""
    TEXT_FILE_PATH = "config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        user_data = json.load(rf)

    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.data_edit = customtkinter.CTkToplevel(master)
        self.data_edit.withdraw()
        self.data_edit.minsize(700, 430)
        self.data_edit.transient(master)
        self.data_edit.title('Modify Data')
        self.data_edit.geometry('850x450+310+130')
        self.data_edit.after(800, self.data_edit.deiconify)

        self.data_edit.columnconfigure(0, weight=1, uniform='a')
        self.data_edit.rowconfigure((1, 2), weight = 1, uniform='a')

        self.top_frame = customtkinter.CTkFrame(self.data_edit, border_width = 0.4,
                                                border_color ='gray20', corner_radius = 4,height=18, fg_color='gray35')
        self.top_frame.grid(row = 0, column = 0, ipady=1, sticky = NSEW)
        self.top_frame.grid_columnconfigure((1, 2, 3), weight = 1)

        self.top_frame_label = customtkinter.CTkLabel(master=self.top_frame,
                                                      text='Daily sales record ID =>',
                                                      font=('Times', 17))
        self.top_frame_label.grid(row=0, column=0, padx=(18, 0), pady=(7, 0))


        self.search_box = customtkinter.CTkEntry(master=self.top_frame, corner_radius=8,
                                                 placeholder_text=self.user_data['entry_search'], 
                                                 width=150, height=30)
        self.search_box.grid(row=0, column=1, padx=(0, 0), pady=(6, 0))

        
        self.search_button = customtkinter.CTkButton(master=self.top_frame, text='',
                                                width=28, height=27, corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', 
                                                image=get_ctk_image(icon='logo_08', size=20),
                                                compound='left', command=self.search_item_id,
                                                border_color='gray40', border_width=1,)
        self.search_button.grid(row=0, column=1, padx=(155, 0), pady=(6, 0))


        self.data_frame = customtkinter.CTkFrame(self.data_edit, width=400, 
                                                 height=500, corner_radius=5)
        self.data_frame.grid(row=1, column=0, padx=(10, 10), rowspan=4, pady=(10, 15),
                             sticky=NSEW)
        self.data_frame.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.data_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')


        tabview = customtkinter.CTkTabview(master=self.data_frame, width=824, height=378,
                                           corner_radius=6, fg_color=('gray20'), border_width=1)
        tabview.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        tabview.add("Edit daily sales")  # add tab at the end
        tabview.add("Edit new stock")  # add tab at the end
        tabview.set("Edit daily sales")  # set currently visible tab

        self.itm = customtkinter.StringVar()
        self.item_sales = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"), 
                                                 width=180, height=32, textvariable=self.itm,
                                                 placeholder_text='Item sold', font=('Sans', 14))
        self.item_sales.place(x=30, y=20)

        self.qtn = customtkinter.StringVar()
        self.quantity = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"),
                                               width=100, height=32, font=('Sans', 14),
                                               textvariable=self.qtn,
                                               placeholder_text='Quantity')
        self.quantity.place(x=225, y=20)

        self.pri = customtkinter.StringVar()
        self.price = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"), 
                                            height=32, textvariable=self.pri, width=100,
                                            placeholder_text=' Price', font=('Sans', 14))
        self.price.place(x=340, y=20)

        self.amt = customtkinter.StringVar()
        self.amount_paid = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"), 
                                                  width=100, height=32, textvariable=self.amt,
                                                  placeholder_text='Amount paid',
                                                  font=('Sans', 14))
        self.amount_paid.place(x=455, y=20)

        self.blc = customtkinter.StringVar()
        self.balance_left = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"), 
                                                   width=180, height=32, textvariable=self.blc,
                                                   placeholder_text='Balance',
                                                   font=('Sans', 14))
        self.balance_left.place(x=30, y=70)

        self.srv = customtkinter.StringVar()
        self.served_by = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"), 
                                                width=100, height=32, textvariable=self.srv,
                                                placeholder_text='Served By',
                                                font=('Sans', 14))
        self.served_by.place(x=225, y=70)

        self.cut = customtkinter.StringVar()
        self.contact = customtkinter.CTkEntry(master=tabview.tab("Edit daily sales"),
                                              width=100, height=32, textvariable=self.cut,
                                              placeholder_text='Customer Contact',
                                              font=('Sans', 13))
        self.contact.place(x=340, y=70)

        self.data_modify = customtkinter.CTkButton(master=tabview.tab("Edit daily sales"),
                                                   width=80, text='Close/Exit',
                                                   height=25, corner_radius=5,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.close_win)
        self.data_modify.place(x=520, y=300)

        self.data_modify = customtkinter.CTkButton(master=tabview.tab("Edit daily sales"),
                                                   width=80, text='Delete Data',
                                                   fg_color='#F24405', height=25,
                                                   corner_radius=5,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.delete_data)
        self.data_modify.place(x=620, y=300)

        self.data_modify = customtkinter.CTkButton(master=tabview.tab("Edit daily sales"),
                                                   text='Update', width=80, height=25,
                                                   corner_radius=5,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.new_update)
        self.data_modify.place(x=720, y=300)

        """--------------End of daily sales-----------------------"""

        self.label_stock = customtkinter.CTkLabel(master=self.top_frame,
                                                      text='New sales record ID =>',
                                                      font=('Times', 17))
        self.label_stock.grid(row=0, column=2, padx=(18, 0), pady=(7, 0))


        self.search_box_stock = customtkinter.CTkEntry(master=self.top_frame, corner_radius=8,
                                                 placeholder_text=self.user_data['entry_search'], 
                                                 width=150, height=30)
        self.search_box_stock.grid(row=0, column=3, padx=(0, 40), pady=(6, 0))

        
        self.search_button_stock = customtkinter.CTkButton(master=self.top_frame, text='',
                                                width=28, height=27, corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', 
                                                image=get_ctk_image(icon='logo_08', size=20),
                                                compound='left', command=self.search_stock_id,
                                                border_color='gray40', border_width=1,)
        self.search_button_stock.grid(row=0, column=3, padx=(90, 0), pady=(6, 0))


        self.itm_stock = customtkinter.StringVar()
        self.item_sales = customtkinter.CTkEntry(master=tabview.tab("Edit new stock"), 
                                                 width=180, height=32, textvariable=self.itm_stock,
                                                 placeholder_text='Item sold', font=('Sans', 14))
        self.item_sales.place(x=30, y=20)

        self.qtn_stock = customtkinter.StringVar()
        self.quantity = customtkinter.CTkEntry(master=tabview.tab("Edit new stock"),
                                               width=100, height=32, font=('Sans', 14),
                                               textvariable=self.qtn_stock,
                                               placeholder_text='Quantity')
        self.quantity.place(x=225, y=20)

        self.pri_stock = customtkinter.StringVar()
        self.price = customtkinter.CTkEntry(master=tabview.tab("Edit new stock"), 
                                            height=32, textvariable=self.pri_stock, width=100,
                                            placeholder_text=' Price', font=('Sans', 14))
        self.price.place(x=340, y=20)

        self.button_modify_stock = customtkinter.CTkButton(master=tabview.tab("Edit new stock"),
                                                   width=80, text='Close/Exit',
                                                   height=25, corner_radius=5,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.close_win)
        self.button_modify_stock.place(x=520, y=300)

        self.data_stock = customtkinter.CTkButton(master=tabview.tab("Edit new stock"),
                                                   width=80, text='Delete Data',
                                                   fg_color='#D94F04', height=25,
                                                   corner_radius=5,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.delete_data_stock)
        self.data_stock.place(x=620, y=300)

        self.data_modify_stock = customtkinter.CTkButton(master=tabview.tab("Edit new stock"),
                                                   text='Update', width=80, height=25,
                                                   corner_radius=5,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.new_update_stock)
        self.data_modify_stock.place(x=720, y=300)

        # self.data_edit.mainloop()

    def close_win(self) -> None:
        msg = CTkMessagebox(title='Exit', message='Do you want exit?\
                            Remember to save your update',
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.data_edit.destroy()
        else:
            return
        
    def search_stock_id(self) -> int:
        itemid = self.search_box_stock.get().lower()
        item = database.fetch_data(itemid)
        try:
            self.itm_stock.set(item[0][0])
            self.qtn_stock.set(item[0][1])
            self.pri_stock.set(item[0][2])
        except IndexError as e:
            CTkMessagebox(title='Not found', 
                          message=f'Record ID not found please try again!  {str(e)}',
                          option_1='Ok', icon='warning')
            
    def new_update_stock(self) -> None:
        connection = sqlite3.connect(resource_path('data__/new_frame.db'))
        conn = connection.cursor()
        itemid = self.search_box_stock.get()
        try:
            conn.execute("""UPDATE 'ds_newframe' SET new_item = ?, 
                            quantity = ?, price = ? WHERE oid = ?""",
                            (self.itm_stock.get(), self.qtn_stock.get(), 
                             self.pri_stock.get(), itemid ))
            connection.commit()
            CTkMessagebox(title='Saved', message='Data updated successfully', 
                          option_1='OK', icon='check')
        except sqlite3.Error as e:
            connection.rollback()
            CTkMessagebox(title='Error', message=f'Data update failed!: {str(e)}', 
                          option_1='OK', icon='cancel')
        finally:
            connection.close()

    def delete_data_stock(self) -> None:
        try:
            connection = sqlite3.connect(resource_path('data__/new_frame.db'))
            conn = connection.cursor()
            if self.search_box_stock.get():
                msg = CTkMessagebox(title='SwiftSell',
                                    message='Are you sure you want to delete this data?', 
                                    option_1='Yes', option_2='No', icon='warning')
                if msg.get() == 'Yes':
                    conn.execute("DELETE FROM 'ds_newframe' WHERE oid = " + 
                                 self.search_box_stock.get())
                    self.search_box_stock.delete(0, END)
                    CTkMessagebox(title='Successfully', message='Data deleted successfully',
                                  option_1='OK', icon='check')
                    connection.commit() 
            else:
                return
        except sqlite3.Error as e:
            CTkMessagebox(title='Error', message=f'There is a problem deleting data: {str(e)}',
                          option_1='OK', icon='cancel')
        finally:
            connection.close()
    """------------------------End of  new stock----------------------------"""

    def search_item_id(self) -> int:
        itemid = self.search_box.get().lower()
        item = database.fetch_data_populate(itemid)
        try:
            self.itm.set(item[0][0])
            self.qtn.set(item[0][1])
            self.pri.set(item[0][2])
            self.amt.set(item[0][3])
            self.blc.set(item[0][4])
            self.srv.set(item[0][5])
            self.cut.set(item[0][6])
        except IndexError as e:
            CTkMessagebox(title='Not found', 
                          message=f'Record ID not found please try again!  {str(e)}',
                          option_1='Ok', icon='warning')

    def new_update(self) -> None:
        connection = sqlite3.connect(resource_path('data__/daily_database.db'))
        conn = connection.cursor()
        itemid = self.search_box.get()
        try:
            conn.execute("""UPDATE data_collection SET item_sales = ?, 
                            quantity = ?, price = ?, amount = ?, balance = ?, 
                            served_by = ?, contact = ? WHERE oid = ?""",
                            (self.itm.get(), self.qtn.get(), self.pri.get(), 
                             self.amt.get(), self.blc.get(), self.srv.get(),
                             self.cut.get(), itemid ))
            connection.commit()
            CTkMessagebox(title='Saved', message='Data updated successfully', 
                          option_1='OK', icon='check')
        except sqlite3.Error as e:
            connection.rollback()
            CTkMessagebox(title='Error', message=f'Data update failed!:  {str(e)}', 
                          option_1='OK', icon='cancel')
        finally:
            connection.close()

    def delete_data(self) -> None:
        try:
            connection = sqlite3.connect(resource_path('data__/daily_database.db'))
            conn = connection.cursor()
            if self.search_box.get():
                msg = CTkMessagebox(title='SwiftSell',
                                    message='Are you sure you want to delete this data?', 
                                    option_1='Yes', option_2='No', icon='warning')
                if msg.get() == 'Yes':
                    conn.execute("DELETE FROM 'data_collection' WHERE oid = " + 
                                 self.search_box.get())
                    self.search_box.delete(0, END)
                    CTkMessagebox(title='Successfully', message='Data deleted successfully',
                                  option_1='OK', icon='check')
                    connection.commit() 
            else:
                return
        except sqlite3.Error as e:
            CTkMessagebox(title='Error', message=f'There is a problem deleting data: {str(e)}',
                          option_1='OK', icon='cancel')
        finally:
            connection.close()


# if __name__ == "__main__":
#     app = EditData()