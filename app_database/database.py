import os
import sys
import sqlite3


"""https://www.sqlite.or/datatype3.html"""

"""https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file"""


global _MEIPASS

def resource_path(relative_path):
    try: # If the script is running in a cx_freeze bundle (i.e. a compiled executable)
        base_path = sys, _MEIPASS
    except Exception:
        """Otherwise, use the current working directory (i.e. the project directory)"""
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    """Join the base path with the relative path to get the absolute path to the resource"""

data_folder = resource_path('data__')
"""Define a variable to hold the path to the 'data__' folder"""
if not os.path.exists(data_folder): #Check if the 'data__' folder exists if not then create it
    os.makedirs(data_folder)
# print(os.path.abspath(os.path.join(sys.executable, '.', 'data__')))
"""Print the absolute path to the 'data__' folder"""

try:
    try:
        """Signup database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'),
                                                  'register.db'))
        conn = connection.cursor()
        conn.execute(""" CREATE TABLE IF NOT EXISTS ds_register(
            Username TEXT,
            Password TEXT,
            Comfirm_password,
            User_role TEXT
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'register.db':", e)

    try:
        """Admin note database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 
                                                  'ds_note.db'))
        conn = connection.cursor()
        conn.execute(""" CREATE TABLE IF NOT EXISTS admin_note(
            Note_title TEXT not null,
            Note_content TEXT not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'ds_note.db':", e)

    try:
        """Admin daily sales database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 
                                                  'ds_admin.db'))
        conn = connection.cursor()
        conn.execute(""" CREATE TABLE IF NOT EXISTS adminsales(
            Daily_sales INTEGER not null,
            Daily_expenses INTEGER not null,
            Item_bought1 TEXT not null,
            Price2 INTEGER not null,
            Item_bought TEXT not null,
            Price4 INTEGER not null,
            Item_bought5 TEXT not null,
            Price6 INTEGER not null,
            Date INTEGER not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'ds_admin.db':", e)

    try:
        """Daily sales database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'),
                                                  'daily_database.db'))
        conn = connection.cursor()
        conn.execute("""CREATE TABLE IF NOT EXISTS data_collection(
            Item_sales TEXT not null,
            Quantity INTEGER not null,
            Price INTEGER not null,
            Amount INTEGER not null,
            Balance TEXT not null,
            Served_by TEXT not null,
            Contact TEXT not null,
            Date INTEGER not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'daily_database.db':", e)

    try:
        """New stock database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 
                                                  'new_frame.db'))
        conn = connection.cursor()
        conn.execute("""CREATE TABLE IF NOT EXISTS ds_newframe(
            New_item TEXT not null,
            Quantity INTEGER not null,
            Price INTEGER not null,
            Date INTEGER not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print(f"Error creating 'new_frame.db': {str(e)}")

except Exception as e:
    print(f"Error connecting to database: {str(e)}")
else:
    print('Database created successfully!!')
# ------------------------End of Database creation--------------------------------

    """This function add data into the register database"""
def create_new_user(Username: str, Password: str, 
                    Comfirm_password: str, User_role: str):
    connection = sqlite3.connect('data__/register.db')
    conn = connection.cursor()
    conn.execute("INSERT INTO 'ds_register' VALUES (?,?,?,?)",
                 (Username, Password, Comfirm_password, User_role))
    connection.commit()
    connection.close()

def admin_note(Note_title: str, Note_content: str):
    """This function add admin note into the database"""
    connection = sqlite3.connect("data__/ds_note.db")
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'admin_note' VALUES (?,?)",
                 (Note_title, Note_content))
    connection.commit()
    connection.close()

    """This function add admin_daily sales into the database"""
def get_data_admin(Daily_sales: int, Daily_expenses: int, 
                   Item_bought1: str, Price2: int,
                   Item_bought3: str, Price4: int, 
                   Item_bought5: str, Price6: int, Date: str = None):
    connection = sqlite3.connect("data__/ds_admin.db")
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'adminsales' VALUES (?,?,?,?,?,?,?,?,?)",
                 (Daily_sales, Daily_expenses, Item_bought1, Price2,
                  Item_bought3, Price4, Item_bought5, Price6, Date))
    connection.commit()
    connection.close()

    """This function add daily sales into the database"""
def insert_daily_sales(Item_sales: int, Quantity: int, Price: int,
                       Amount: int, balance: str, served_by: str,
                       contact: int,  date: str = None):
    connection = sqlite3.connect('data__/daily_database.db')
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'data_collection' VALUES (?,?,?,?,?,?,?,?)",
                 (Item_sales, Quantity, Price, Amount, 
                  balance, served_by, contact, date))
    connection.commit()
    connection.close()

"""This function also add new stock into the database"""
def new_stock(Newitem: str, Quantity: int,
              Price: int, Date: str = None):
    connection = sqlite3.connect("data__/new_frame.db")
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'ds_newframe' VALUES (?,?,?,?)",
                 (Newitem, Quantity, Price, Date))
    connection.commit()
    connection.close()

def fetch_data_populate(rowid: int):
    """This function is use to fetch, and populate data into update table"""
    connection = sqlite3.connect('data__/daily_database.db')
    conn = connection.cursor()
    conn.execute("SELECT * FROM 'data_collection' WHERE rowid=?", (rowid,))
    return conn.fetchall()

def fetch_data(rowid: int):
    """Fetch all records in daily sales report."""
    connection = sqlite3.connect('data__/new_frame.db')
    conn = connection.cursor()
    conn.execute("SELECT * FROM 'ds_newframe' WHERE rowid=?", (rowid,))
    return conn.fetchall()


#================Requesting or fetching data from the database================
# try:
#     connection = sqlite3.connect('daily_database.db')
#     conn = connection.cursor()
#     conn.execute("""CREATE TABLE IF NOT EXISTS data_collection(
#         id INTEGER PRIMARY KEY,
#         item_sales TEXT not null,
#         quantity INTEGER not null,
#         price INTEGER not null,
#         amount INTEGER not null,
#         balance INTEGER not null,
#         served_by TEXT not null,
#         contact TEXT not null,
#         date INTEGER not null,
#         new_frame_id INTEGER,
#         FOREIGN KEY (new_frame_id) REFERENCES ds_newframe(id)
#         )""")
#     connection.commit()
#     connection.close()

#     # Create new stock database
#     connection = sqlite3.connect('new_frame.db')
#     conn = connection.cursor()
#     conn.execute("""CREATE TABLE IF NOT EXISTS ds_newframe(
#         id INTEGER PRIMARY KEY,
#         new_item TEXT not null,
#         quantity INTEGER not null,
#         price INTEGER not null,
#         date INTEGER not null
#         )""")
#     connection.commit()
#     connection.close()

#     # Insert a new stock item and link it to a daily sale
#     connection = sqlite3.connect('daily_database.db')
#     conn = connection.cursor()
#     conn.execute("INSERT INTO 'data_collection' VALUES (?,?,?,?,?,?,?,?,?,?)",
#                 (1, 'item 1', 2, 10, 20, 0, 'user1', '12345', 1647904000, 1))
#     connection.commit()
#     connection.close()

#     connection = sqlite3.connect('new_frame.db')
#     conn = connection.cursor()
#     conn.execute("INSERT INTO 'ds_newframe' VALUES (?,?,?,?,?)",
#                 (1, 'new item 1', 5, 15, 1647904000))
#     connection.commit()
#     connection.close()
# except ValueError:
#     pass



"""this code is use to update the database"""
# def new_update(self):
#     connection = sqlite3.connect('daily_database.db')
#     conn = connection.cursor()
#     itemid = self.search_box.get()
#     try:
#         conn.execute(""" UPDATE data_collection SET 
#                         item_sales = :item_sales,
#                         quantity = :quantity,
#                         price = :price,
#                         amount = :amount,
#                         balance = :balance,
#                         served_by = :served_by,
#                         contactf = :contact
#                         WHERE oid = :oid""",
#                         {'item_sales': self.itm.get(),
#                          'quantity': self.qtn.get(),
#                          "price": self.pri.get(),
#                          "amount": self.amt.get(),
#                          "balance": self.blc.get(),
#                          "served_by": self.srv.get(),
#                          "contact": self.cut.get(),
#                          "oid": itemid
#                         })
#         connection.commit()
#         CTkMessagebox(title='Saved', message='Data updated successfully', 
#                       option_1='OK', icon='check')
#     except sqlite3.Error as e:
#         connection.rollback()
#         CTkMessagebox(title='Error', 
#           message=f'Data update failed: {str(e)}', 
#           option_1='OK', icon='error')
#     finally:
#         connection.close()

