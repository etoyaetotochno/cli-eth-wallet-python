import db

# Автентифікація облікового запису
def authenticate(username, password):
    user = db.get_user(username)
    if user and user['password'] == password:
        return user
    else:
        return None