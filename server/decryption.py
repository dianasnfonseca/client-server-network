from cryptography.fernet import Fernet

def decrypt_data(data, encryption_key):
    """
    Decrypt data using the Fernet symmetric encryption algorithm.

    Args:
        data (bytes): Encrypted data to be decrypted.
        encryption_key (bytes): Encryption key used for decryption.

    Returns:
        bytes: Decrypted data.
    """
    try:
        # Create a Fernet cipher object with the encryption key
        cipher = Fernet(encryption_key)

        # Decrypt the data
        decrypted_data = cipher.decrypt(data)

        return decrypted_data
    except Exception as e:
        # Handle decryption errors
        print(f"Decryption error: {e}")
        return None
