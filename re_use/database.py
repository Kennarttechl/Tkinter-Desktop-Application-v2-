import sqlite3


# CONNECT = sqlite3.connect(":memory:")
connection = sqlite3.connect('data_collection.db')
conn = connection.cursor() #This tell the database what you want to do


# ================Deleting a table or Droping a table=============
# conn.execute("""DROP TABLE data_collection""")
# connection.commit()
# ==============================================================


# ==================Query the database -> BY LIMITING IT=================
# conn.execute("""SELECT rowid, * FROM data_collection LIMIT 1""")
# conn.execute("""SELECT rowid, * FROM data_collection 
#                 ORDER BY rowid DESC LIMIT 1"""
#              )
# ======================================================================


# =====================Query the database -> AND/OR=================
# conn.execute("""SELECT rowid, * FROM data_collection WHERE 
#             last_name LIKE 'Br%' AND rowid = 4""")

# conn.execute("""SELECT rowid, * FROM data_collection WHERE 
#             last_name LIKE 'Br%' OR rowid = 4""")
# ==============================================================


# ================Query the database -> ORDER BY====================
# conn.execute("SELECT rowid, * FROM data_collection ORDER BY rowid ASC")
# conn.execute("SELECT rowid, * FROM data_collection ORDER BY rowid DESC")
# ==============================================================


# ========================Deleting Record===========================
# conn.execute("""DELETE from data_collection WHERE rowid = 3
#             """)
# connection.commit()
# ==============================================================


# ========================Updating Record==========================
# conn.execute("""UPDATE data_collection SET first_name = 'Bob'
#             WHERE last_name = 'Elder'

#             """)

# conn.execute("""UPDATE data_collection SET first_name = 'Kenn'
#             WHERE rowid = 1

#             """)
# connection.commit()
# ==============================================================


# conn.execute("SELECT * FROM data_collection")
# ============Fetching data from the database using a certain command=================
# conn.execute("SELECT * FROM data_collection WHERE last_name = 'Joan'")
# conn.execute("SELECT * FROM data_collection WHERE age >= 21 ")
# conn.execute("SELECT * FROM data_collection WHERE last_name LIKE 'Br%' ")
# conn.execute("SELECT * FROM data_collection WHERE email LIKE '%gmail.com' ")
# conn.execute("SELECT rowid, * FROM data_collection") #this spit out the row id
# ==============================================================

items = conn.fetchall()
# print(conn.fetchone()[2])
# print(conn.fetchmany(3))

for item in (items):
    # print(i[0] + ' ' + i[1] + ' \t' + i[2])
    print(item)


# =======================Inserting many data manualy===============
# many_data = [
#                 ('John', 'Elder', 'john@gmail.com'), 
#                 ('Tim', 'Smit', 'tim@gmail.com'), 
#                 ('Mary', 'Brwon', 'mary@gmail.com'),
#                 ('Wes', 'Brown', 'wes@codemy.com'),
#             ]
# conn.executemany("INSERT INTO data_collection VALUES (?,?,?)", many_data)
# connection.commit()
# ==================================================================


# =======================Inserting into the database manualy====================
# conn.execute("INSERT INTO data_collection VALUES ('Lynn', 'Joan', 'kentecht@gmail.com')")
# print(f'Data successfully submitted')
# ==============================================================


# =======================Creating table=========================
# conn.execute("""CREATE TABLE data_collection(
#                 first_name text,
#                 last_name text,
#                 email text
#                 )""")
# ==============================================================

# connection.commit()
connection.close()


"""
NULL,
INTEGER,
REAL,
TEXT
BLOB
"""