import socket
import configparser
from serialization import deserialize_data
from decryption import decrypt_data
from logging import log_data

# Load server configuration
config = configparser.ConfigParser()
config.read('config/server_config.ini')

SERVER_IP = config['SERVER']['IP']
SERVER_PORT = int(config['SERVER']['PORT'])

def receive_data():
    """
    Receive data from clients, decrypt, deserialize, and log it.

    Args:
        None

    Returns:
        None
    """
    try:
        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Bind to IP and port
            server_socket.bind((SERVER_IP, SERVER_PORT))
            # Listen for incoming connections
            server_socket.listen()

            print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

            # Accept client connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # Receive data from client
            encrypted_data = client_socket.recv(1024)
            print("Data received from client")

            # Decrypt and deserialize data
            decrypted_data = decrypt_data(encrypted_data)
            data = deserialize_data(decrypted_data)

            # Log data
            log_data(data)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    receive_data()
