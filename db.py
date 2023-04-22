import sqlite3
import crypto
import hashlib

# Файл бази даних
DB_FILENAME = 'wallet.db'

def create_table():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username text, password text, address text, private_key text)''')
    conn.commit()
    conn.close()

def add_user(username, password, address, private_key):
    private_key = crypto.encrypt_private_key(private_key, password)
    password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, password, address, private_key))
    conn.commit()
    conn.close()

def authenticate(username, password):
    password = hashlib.sha256(password.encode()).hexdigest()
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

def get_private_key(username, password, address):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT private_key FROM users WHERE address = ? AND username = ?", (address, username,))
    result = c.fetchone()
    conn.close()
    private_key = crypto.decrypt_private_key(result[0], password)
    return private_key
