from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

def write_key_to_file(key, filename='config/encryption_key.txt'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    # Generate encryption key
    key = generate_key()

    # Write encryption key to file
    write_key_to_file(key)

    print("Encryption key generated and saved to 'config/encryption_key.txt'")
