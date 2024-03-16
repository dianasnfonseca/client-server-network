from cryptography.fernet import Fernet

def decrypt_data(data):
    """
    Decrypt data using the Fernet symmetric encryption algorithm.

    Args:
        data (bytes): Encrypted data to be decrypted.

    Returns:
        bytes: Decrypted data.
    """
    try:
        # Create a Fernet cipher object with the encryption key
        cipher = Fernet(ENCRYPTION_KEY)

        # Decrypt the data
        decrypted_data = cipher.decrypt(data)

        return decrypted_data
    except Exception as e:
        # Handle decryption errors
        print(f"Decryption error: {e}")
        return None
