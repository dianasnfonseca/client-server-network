import socket
import configparser
from serialization import deserialize_data
from decryption import decrypt_data
from logging import log_data

# Load server configuration
config = configparser.ConfigParser()
config.read('config/server_config.ini')

# Extract server IP and port from configuration
#SERVER_IP = config['SERVER']['IP']
SERVER_IP = '127.0.0.1'  # Change this to your machine's IP address if needed
SERVER_PORT_STRING = config['SERVER']['PORT'].strip()
SERVER_PORT = int(''.join(filter(str.isdigit, SERVER_PORT_STRING)))

def receive_data(client_socket, encryption_key):
    """
    Receive data from clients, decrypt, deserialize, and log it.

    Args:
        client_socket: Socket object for the client connection
        encryption_key: Encryption key used for decryption

    Returns:
        None
    """
    try:
        # Receive encrypted data from the client
        encrypted_data = client_socket.recv(1024)

        # Decrypt the received data
        decrypted_data = decrypt_data(encrypted_data, encryption_key)

        # Assuming decrypted_data contains a dictionary
        if decrypted_data:
            # Deserialize the decrypted data
            data = deserialize_data(decrypted_data)
            # Log data
            log_data(data)
        else:
            print("Decryption failed. Unable to process the data.")

    except Exception as e:
        print(f"Error occurred during data reception and processing: {e}")

if __name__ == "__main__":
    # Load server configuration
    config = configparser.ConfigParser()
    config.read('config/server_config.ini')

    # Extract encryption key from configuration
    encryption_key_path = config['ENCRYPTION']['KEY_PATH']
    with open(encryption_key_path, 'rb') as key_file:
        encryption_key = key_file.read()

    try:
        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Bind socket to server address
            server_socket.bind((SERVER_IP, SERVER_PORT))
            # Listen for incoming connections
            server_socket.listen(5)
            print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

            while True:  # Keep the server running indefinitely
                # Accept incoming connection
                client_socket, client_address = server_socket.accept()
                print(f"Connection established with {client_address}")
                # Receive and process data from the client
                receive_data(client_socket, encryption_key)

    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")