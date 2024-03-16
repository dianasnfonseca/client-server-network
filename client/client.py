import socket
import configparser
from serialization import serialize_data
from encryption import encrypt_data

# Load client configuration
config = configparser.ConfigParser()
config.read('config/client_config.ini')

# Extract server IP and port from configuration
#SERVER_IP = config['SERVER']['IP']
SERVER_IP = '127.0.0.1'  # Change this to your machine's IP address if needed
SERVER_PORT_STRING = config['SERVER']['PORT'].strip()
SERVER_PORT = int(''.join(filter(str.isdigit, SERVER_PORT_STRING)))

def send_data(data):
    """
    Send data to the server.

    Args:
        data: Data to be sent to the server

    Returns:
        None
    """
    try:
        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to server
            client_socket.connect((SERVER_IP, SERVER_PORT))

            # Serialize and encrypt data
            serialized_data = serialize_data(data)
            encrypted_data = encrypt_data(serialized_data)

            # Send encrypted data to server
            client_socket.sendall(encrypted_data)
            print("Data sent successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Sample data to send
    data = {'name': 'Diana', 'role': 'SD & tester'}
    send_data(data)
