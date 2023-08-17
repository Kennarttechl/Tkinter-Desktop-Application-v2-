import sqlite3
import pandas as pd
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox

global df
def export_data_excela():
    """ Function to export data to `EXCEL` and read data from database into a 
    pandas DataFrame """
    try:
        connection = sqlite3.connect('data__/ds_admin.db')
        df = pd.read_sql_query("SELECT * FROM adminsales", connection)
        connection.close()
    except pd.io.sql.DatabaseError as e:
        print('There is a problem connecting to the database:', e)

    """directory path to save the excel file"""
    dir_path = filedialog.askdirectory()

    try:
        """ Write data to an Excel file"""
        file_path = f"{dir_path}/Admin Data.xlsx"
        writer = pd.ExcelWriter(file_path)
        df.to_excel(writer, index=False)
        writer.close()
    except Exception as e:
        CTkMessagebox(title="Error", 
                      message="Error exporting data to Excel: {}".format(str(e)), 
                      option_1='Ok', icon='cancel')
        return
    CTkMessagebox(title="Success", message="Data exported successfully", 
                  option_1='Ok', icon='check')
    

def export_data_exceld():
    try:
        connection = sqlite3.connect("data__/daily_database.db")
        df = pd.read_sql_query("SELECT * FROM data_collection", connection)
        connection.close()
    except pd.io.sql.DatabaseError as e:
        print('There is a problem connecting to the database:', e)
        
    dir_path = filedialog.askdirectory()

    try:
        file_path = f"{dir_path}/Daily Sales.xlsx"
        writer = pd.ExcelWriter(file_path)
        df.to_excel(writer, index=False)
        writer.close()
    except Exception as e:
        CTkMessagebox(title="Error", 
                      message="Error exporting data to Excel: {}".format(str(e)), 
                      option_1='Ok', icon='cancel')
        return
    CTkMessagebox(title="Success", message="Data exported successfully", 
                  option_1='Ok', icon='check')
    

def export_data_excels():
    try:
        connection = sqlite3.connect("data__/new_frame.db")
        df = pd.read_sql_query("SELECT * FROM ds_newframe", connection)
        connection.close()
    except pd.io.sql.DatabaseError as e:
        print('There is a problem connecting to the database:', e)
        
    dir_path = filedialog.askdirectory()
    
    try:
        file_path = f"{dir_path}/New Stock.xlsx"
        writer = pd.ExcelWriter(file_path)
        df.to_excel(writer, index=False)
        writer.close()
    except Exception as e:
        CTkMessagebox(title="Error", 
                      message="Error exporting data to Excel: {}".format(str(e)), 
                      option_1='Ok', icon='cancel')
        return
    CTkMessagebox(title="Success", message="Data exported successfully", 
                  option_1='Ok', icon='check')
    