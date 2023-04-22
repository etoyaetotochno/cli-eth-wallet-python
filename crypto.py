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

def encrypt_private_key(private_key_hex, password):
    private_key_hex = private_key_hex[2:]
    key, salt = generate_key_from_password(password)
    f = Fernet(key)
    private_key_bytes = bytes.fromhex(private_key_hex)
    encrypted_private_key = f.encrypt(private_key_bytes)
    return encrypted_private_key.decode() + "." + salt

def decrypt_private_key(encrypted, password):
    encrypted_private_key, salt = encrypted.split(".")
    salt = bytes.fromhex(salt)
    key, salt = generate_key_from_password(password, salt)
    f = Fernet(key)
    private_key_bytes = f.decrypt(encrypted_private_key)
    return "0x" + private_key_bytes.hex()

