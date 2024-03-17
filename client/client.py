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
        # Load client configuration
        config = configparser.ConfigParser()
        config.read('config/client_config.ini')

        # Extract server IP and port from configuration
        SERVER_IP = '127.0.0.1'
        SERVER_PORT_STRING = config['SERVER']['PORT'].strip()
        SERVER_PORT = int(''.join(filter(str.isdigit, SERVER_PORT_STRING)))

        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Set SO_REUSEADDR option
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Connect to server
            client_socket.connect((SERVER_IP, SERVER_PORT))
            print("Connected to server.")

            # Serialize data based on chosen format
            serialized_data = serialize_data(data, serialization_format)
            
            # Print the serialization format and data
            print(f"Data serialized to {serialization_format.upper()} format:", serialized_data)

            # Combine serialization format and length of serialized data
            message = f"{serialization_format} {len(serialized_data)}"
            client_socket.sendall(message.encode())
            print("Serialization format and length sent to server:", message)

            # Send serialized data to server
            client_socket.sendall(serialized_data)
            print("Serialized data sent to server.")

            # Send file data to server if provided
            if file_path:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    if encrypt_file:
                        # Load encryption key from file
                        encryption_key_path = config['ENCRYPTION']['KEY_PATH']
                        with open(encryption_key_path, 'rb') as key_file:
                            encryption_key = key_file.read()

                        # Encrypt file data if specified
                        encrypted_file_data = encrypt_data(file_data, encryption_key)
                        if encrypted_file_data:
                            file_length = len(encrypted_file_data)
                            client_socket.sendall(str(file_length).encode())  # Convert to string
                            client_socket.sendall(encrypted_file_data)
                            print("Encrypted file data sent to server.")
                    else:
                        file_length = len(file_data)
                        client_socket.sendall(str(file_length).encode())  # Convert to string
                        client_socket.sendall(file_data)
                        print("File data sent to server.")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket connection
        client_socket.close()

if __name__ == "__main__":
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