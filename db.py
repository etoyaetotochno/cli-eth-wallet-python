import sqlite3

# Файл бази даних
DB_FILENAME = 'wallet.db'

# Створення бази даних якщо не існує
def create_table():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username text, password text, address text, private_key text)''')
    conn.commit()
    conn.close()

