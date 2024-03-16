import hashlib
from cryptography.fernet import Fernet

# Load encryption key from configuration file
with open('config/encryption_key.txt', 'rb') as key_file:
    ENCRYPTION_KEY = key_file.read()

def encrypt_data(data):
    """
    Encrypts data using the Fernet symmetric encryption algorithm.

    Args:
        data: Bytes-like object representing data to be encrypted.

    Returns:
        bytes: Encrypted data.
    """
    try:
        # Create a Fernet cipher object with the encryption key
        cipher = Fernet(ENCRYPTION_KEY)

        # Encrypt the data
        encrypted_data = cipher.encrypt(data)

        return encrypted_data
    except Exception as e:
        # Handle encryption errors
        print(f"Encryption error: {e}")
        return None
