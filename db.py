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

# Додання нового користувача в БД
def add_user(username, password, address, private_key):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, password, address, private_key))
    conn.commit()
    conn.close()

# Отримання інформації користувача
def get_user(username):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    if user:
        return {'username': user[0], 'password': user[1], 'address': user[2], 'private_key': user[3]}
    else:
        return None

def user_unique(username):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    exists = False if result else True
    conn.commit()
    conn.close()
    return exists
    
