import os
from cryptography.fernet import Fernet

key_path = os.path.expanduser("~/.psmgr/fernet.key")

def _ensure_key_dir_exists():
    directory = os.path.dirname(key_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def generate_key():
    _ensure_key_dir_exists()
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
    
    return key

def load_key():
    if not os.path.exists(key_path):
        return generate_key()
    with open(key_path, "rb") as f:
        key = f.read().decode().strip()
        if key:
            return key
        else:
            generate_key()
            load_key()

def get_fernet():
    return Fernet(load_key())

