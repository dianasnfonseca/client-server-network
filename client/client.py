# client.py
import socket
import configparser
from serialization import serialize_data
from encryption import encrypt_data

def send_data(data, serialization_format, file_path=None, encrypt_file=False):
    """
    Send serialized data along with serialization format to the server.

    Args:
        data: Data (dictionary) to be sent to the server.
        serialization_format (str): Serialization format chosen by the user.
        file_path (str): Path to the file to be sent (optional).
        encrypt_file (bool): Flag indicating whether to encrypt the file data.

    Returns:
        None
    """
    try:
        config = configparser.ConfigParser()
        config.read('config/client_config.ini')

        server_ip = '127.0.0.1'
        server_port_string = config['SERVER']['PORT'].strip()
        server_port = int(''.join(filter(str.isdigit, server_port_string)))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            client_socket.connect((server_ip, server_port))

            serialized_data = serialize_data(data, serialization_format)

            message = f"{serialization_format} {len(serialized_data)}"
            client_socket.sendall(message.encode())

            client_socket.sendall(serialized_data)

            encryption_key_path = config['ENCRYPTION']['KEY_PATH']
            with open(encryption_key_path, 'rb') as key_file:
                encryption_key = key_file.read()

            if file_path:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    if encrypt_file:
                        encrypted_file_data = encrypt_data(file_data, encryption_key)
                        if encrypted_file_data:
                            file_length = len(encrypted_file_data)
                            client_socket.sendall(str(file_length).encode())
                            client_socket.recv(1024)
                            client_socket.sendall(encrypted_file_data)
                    else:
                        file_length = len(file_data)
                        client_socket.sendall(str(file_length).encode())
                        client_socket.recv(1024)
                        client_socket.sendall(file_data)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if client_socket:
            # Close the socket connection
            client_socket.close()

if __name__ == "__main__":
    try:
        # Sample data to send
        data = {'name': 'Diana', 'role': 'SD & tester'}

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

        # Prompt user for file path and encryption option
        file_path = input("Enter file path to send (leave blank to skip): ")
        encrypt_choice = input("Encrypt file? (yes/no): ").lower()
        encrypt_file = encrypt_choice == 'yes'

        # Send data with chosen format and optional file encryption
        send_data(data, serialization_format, file_path, encrypt_file)

    except Exception as e:
        print(f"Error occurred: {e}")
