from cryptography.fernet import Fernet

# Generate a Fernet key
key = Fernet.generate_key()

# Save the key to a file
with open('encryption_key.txt', 'wb') as key_file:
    key_file.write(key)