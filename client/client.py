import socket
import configparser
from serialization import serialize_data
from encryption import encrypt_data  # Import the encryption function

def send_data(data, filename):
    """
    Send serialized and encrypted data along with file contents to the server.

    Args:
        data: Data (dictionary) to be sent to the server.
        filename (str): Name of the file to send.

    Returns:
        None
    """
    try:
        # Load client configuration
        config = configparser.ConfigParser()
        config.read('config/client_config.ini')

        # Extract server IP and port from configuration
        SERVER_IP = '127.0.0.1'
        SERVER_PORT_STRING = config['SERVER']['PORT'].strip()
        SERVER_PORT = int(''.join(filter(str.isdigit, SERVER_PORT_STRING)))

        # Prompt user for serialization format choice
        print("Choose serialization format:")
        print("1. JSON")
        print("2. XML")
        print("3. Binary")
        choice = input("Enter your choice (1/2/3): ")

        # Map user choice to serialization format
        if choice == '1':
            serialization_format = 'json'
        elif choice == '2':
            serialization_format = 'xml'
        elif choice == '3':
            serialization_format = 'binary'  # Modify this if you have a specific binary format
        else:
            print("Invalid choice. Using default format (JSON).")
            serialization_format = 'json'

        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to server
            client_socket.connect((SERVER_IP, SERVER_PORT))
            print("Connected to server.")

            # Serialize data based on chosen format
            serialized_data = serialize_data(data, serialization_format)
            print("Data serialized.")

            # Encrypt the serialized data
            encrypted_data = encrypt_data(serialized_data)
            print("Data encrypted.")

            # Read file contents
            with open(filename, 'rb') as file:
                file_data = file.read()

            # Send serialization format to server
            client_socket.sendall(serialization_format.encode())
            print("Serialization format sent to server.")

            # Send encrypted data to server
            client_socket.sendall(encrypted_data)
            print("Encrypted data sent to server.")

            # Send file data to server
            client_socket.sendall(file_data)
            print("File data sent to server.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Sample data to send
    data = {'name': 'Diana', 'role': 'SD & tester'}
    filename = "sample.txt"

    # Send data with chosen format
    send_data(data, filename)
