import sqlite3
from CTkMessagebox import CTkMessagebox
from app_database.database import resource_path


def load_data():
    try:
        connection = sqlite3.connect(resource_path('data__/new_frame.db'))
        conn = connection.cursor()
        conn.execute("SELECT * FROM ds_newframe")
        rows = conn.fetchall()

        if len(rows) == 0:
            return None

        colums = [description[0] for description in conn.description]
        serialized_data = []

        for row in rows:
            serialized_data.append(dict(zip(colums, row)))

        connection.commit()
        return serialized_data
    except sqlite3.Error as e:
        CTkMessagebox(title='Error', 
                      message=f'There was a problem fetching the data: {str(e)}',
                      option_1='cancel')
    finally:
        connection.close()