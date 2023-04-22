import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

def random_string(length):
    random_string = secrets.token_bytes(length)
    return random_string

def generate_key_from_password(password, salt=None):
    if not salt:
        salt = random_string(16)
    elif type(salt) == str:
        salt = bytes.fromhex(salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key), salt.hex()

