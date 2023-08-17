import sqlite3
from CTkMessagebox import CTkMessagebox



def show_all():
    """Query the DB and Return all Records"""
    connection = sqlite3.connect('student.db')
    conn = connection.cursor()
    conn.execute("""SELECT rowid, * FROM customer""")
    items = conn.fetchall()

    for item in items:
        print(item)
# show_all()


    # conn.execute("INSERT INTO customer VALUES ('Kenn', 'Mawuli', 'mawuli@gmail.com')")
    # connection.commit()
    # print('value sent successfully')


def create_database(id, name, password, telephone, address):
    connnection = sqlite3.connect('student.db')
    conn = connnection.cursor()
    conn.execute("""CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY, 
                 name TEXT
                 password REAL
                 telephone REAL 
                 address TEXT
                 )""", (id, name, password, telephone, address))
    connnection.commit()
    connnection.close()
# create_database(1, 'w', 'e', 'e', 'e')



def update_record(id, name, password, telephone, address):
    connection = sqlite3.connect('student.db')
    conn = connection.cursor()
    conn.execute("UPDATE students SET telephone=? WHERE id=?", 
    (id, name, password, telephone, address))
    connection.commit()
    connection.close()


try:
    connection = sqlite3.connect('student.db')
    conn = connection.cursor()
    conn.execute("""CREATE TABLE IF NOT EXISTS customer(
                id INTEGER PRIMARY KEY,
                first_name text,
                last_name text,
                email text
                )""")
    connection.commit()
    connection.close()
except ValueError:
    print('there was a problem')
else:
    print('created well')


def email_lookup(id):
    connection = sqlite3.connect('student.db')
    conn = connection.cursor()
    conn.execute("SELECT id, * from customer WHERE id = (?)", (id,))
    # conn.execute("SELECT * from customer WHERE email = (?)", (email,))
    items = conn.fetchall()

    for item in items:
        print(item)
email_lookup(3)


def add_many(list):
    connection = sqlite3.connect('app.db')
    conn = connection.cursor()
    conn.executemany("INSERT INTO customer VALUES (?,?,?)", (list))
    connection.commit()
    connection.close()

# my_grocery_store = [
#                 ('banana', 'mango', 'ornage'),
#                 ('pinneaple', 'grapes', 'milk'),
#                 ('julien', 'brenda', 'timatoes')
#                 ]
# add_many(my_grocery_store)


def add_one(id, first, last, email) -> None:
    connection = sqlite3.connect('student.db')
    conn = connection.cursor()
    conn.execute("INSERT INTO customer VALUES (?,?,?,?)", (id, first, last, email))
    connection.commit()
    connection.close()
# add_one(5, 'Laura', 'azameti', 'gh@gmail.com')


"""Or"""
def add_one(first, last, email: str='nss@gmail.com') -> None:
    connection = sqlite3.connect('app.db')
    conn = connection.cursor()
    conn.execute("INSERT INTO customer VALUES (?,?,?)", (first, last, email))
    print(type(email))
    connection.commit()
    connection.close()
# add_one('Laura', 'azameti')


def delete_one(id) -> None:
    connection = sqlite3.connect('app.db')
    conn = connection.cursor()
    conn.execute("DELETE from customer WHERE rowid = (?)", (id)) #or id
    connection.commit()
    connection.close()
"""Delete record use rowid as string"""
# delete_one('5')



