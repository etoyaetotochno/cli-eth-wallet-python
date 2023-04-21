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
def authenticate(username, password):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT username, password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    if user and password == user[1]:
        return True
    else:
        return False

def user_unique(username):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT username FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    exists = False if result else True
    conn.close()
    return exists
    
def check_address(username, address):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT address FROM users WHERE username = ? AND address = ?", (username, address,))
    result = c.fetchone()
    exists = True if result else False
    conn.close()
    return exists

def user_addresses(username):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT address FROM users WHERE username = ?", (username,))
    result = c.fetchall()
    conn.close()
    return result

def get_private_key(address):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT private_key FROM users WHERE address = ?", (address,))
    result = c.fetchall()
    conn.close()
    return result
