import socket
import configparser
from serialization import deserialize_data
from decryption import decrypt_data

def receive_data(client_socket, config):
    """
    Receive data from the client, deserialize it, and decrypt file data if necessary.

    Args:
        client_socket (socket.socket): Client socket object.
        config (configparser.ConfigParser): Configuration object.

    Returns:
        None
    """
    try:
        # Receive serialization format and length of serialized data from the client
        format_length_data = client_socket.recv(1024).decode().strip()
        print("Received data from client:", format_length_data)

        # Split the received data into serialization format and length
        parts = format_length_data.split(" ")
        if len(parts) != 2:
            print("Invalid format received from client.")
            return

        format_choice, length_data = parts
        print("Serialization format received from client:", format_choice)
        print("Received length data:", length_data)
        
        # Convert length_data to integer
        length = int(length_data)
        print("Length of serialized data:", length)

        # Receive serialized data from the client
        serialized_data = b""
        while len(serialized_data) < length:
            chunk = client_socket.recv(min(length - len(serialized_data), 1024))
            if not chunk:
                break
            serialized_data += chunk
        
        print(f"Serialized data received from client ({len(serialized_data)} bytes):", serialized_data)

        # Process received data
        data = deserialize_data(serialized_data, format_choice)
        if data:
            print("Received dictionary:", data)

        # Receive file if sent
        file_length = int(client_socket.recv(1024).decode())
        print("Length of file data:", file_length)
        file_data = b""
        while len(file_data) < file_length:
            chunk = client_socket.recv(min(file_length - len(file_data), 1024))
            if not chunk:
                break
            file_data += chunk
        print("File data received from client:", file_data)

        # Decrypt the file data if encrypted
        decrypt_file_str = config['SERVER']['DECRYPT_FILE']
        decrypt_file = decrypt_file_str.lower() == 'true'
        if decrypt_file:
            encryption_key_path = config['ENCRYPTION']['KEY_PATH']
            with open(encryption_key_path, 'rb') as key_file:
                encryption_key = key_file.read()
            decrypted_file_data = decrypt_data(file_data, encryption_key)
            print("Decrypted file data:", decrypted_file_data.decode())

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    try:
        # Load server configuration
        config = configparser.ConfigParser()
        config.read('config/server_config.ini')

        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Set SO_REUSEADDR option
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Extract server IP and port from configuration
            server_ip = '127.0.0.1'
            server_port_string = config['SERVER']['PORT'].strip()
            server_port = int(''.join(filter(str.isdigit, server_port_string)))

            # Bind socket to server address
            server_socket.bind((server_ip, server_port))
            # Listen for incoming connections
            server_socket.listen(5)
            print(f"Server is listening on {server_ip}:{server_port}")

            while True:  # Keep the server running indefinitely
                # Accept incoming connection
                client_socket, client_address = server_socket.accept()
                print(f"Connection established with {client_address}")

                # Receive and process data from the client
                receive_data(client_socket, config)

    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")
