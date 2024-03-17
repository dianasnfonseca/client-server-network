from cryptography.fernet import Fernet

# Load encryption key from configuration file
with open('config/encryption_key.txt', 'rb') as key_file:
    ENCRYPTION_KEY = key_file.read()

def encrypt_data(data, encryption_key):
    """
    Encrypts data using the Fernet symmetric encryption algorithm.

    Args:
        data: Bytes-like object representing data to be encrypted.
        encryption_key (bytes): Encryption key used for encryption.

    Returns:
        bytes: Encrypted data.
    """
    try:
        # Create a Fernet cipher object with the encryption key
        cipher = Fernet(encryption_key)

        # Encrypt the data
        encrypted_data = cipher.encrypt(data)

        return encrypted_data
    except Exception as e:
        # Handle encryption errors
        print(f"Encryption error: {e}")
        return None
