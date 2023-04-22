import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def random_string(length):
    random_string = secrets.token_bytes(length)
    return random_string

