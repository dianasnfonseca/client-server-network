import os
import uuid
from cryptography.fernet import Fernet

def generate_key(seed=None):
    if seed is None:
        seed = uuid.uuid4().bytes
    return Fernet.generate_key(seed)

def write_key_to_file(key, filename='config/encryption_key.txt'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def copy_key_to_server(key):
    server_key_path = '../server/config/encryption_key.txt'
    write_key_to_file(key, server_key_path)
    print(f"Encryption key copied to '{server_key_path}'")

if __name__ == "__main__":
    # Generate encryption key with a new seed (unique identifier)
    key = generate_key()

    # Write encryption key to file
    write_key_to_file(key)

    # Copy encryption key to the server folder
    copy_key_to_server(key)

    print("Encryption key generated and saved to 'config/encryption_key.txt'")
