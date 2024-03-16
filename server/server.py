import socket
import json  # Import JSON module for deserialization
import configparser

def deserialize_data(serialized_data):
    """
    Deserialize JSON string to data (dictionary).

    Args:
        serialized_data (str): Serialized data (JSON string).

    Returns:
        dict: Deserialized data (dictionary).
    """
    return json.loads(serialized_data)

def receive_data(client_socket):
    """
    Receive and deserialize data from the client.

    Args:
        client_socket: Socket object for the client connection.

    Returns:
        dict: Deserialized data (dictionary).
        bytes: Contents of the text file.
    """
    try:
        # Receive serialized data from the client (dictionary)
        serialized_data = client_socket.recv(1024).decode()
        print("Dictionary received from client")

        # Deserialize the received data (JSON string to dictionary)
        data = deserialize_data(serialized_data)

        # Receive file data from the client
        file_data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            file_data += chunk

        print("File received from client")
        
        return data, file_data

    except Exception as e:
        print(f"Error occurred during data reception: {e}")
        return None, None

if __name__ == "__main__":
    try:
        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Load server configuration
            config = configparser.ConfigParser()
            config.read('config/server_config.ini')

            # Extract server IP and port from configuration
            SERVER_IP = '127.0.0.1'
            SERVER_PORT_STRING = config['SERVER']['PORT'].strip()
            SERVER_PORT = int(''.join(filter(str.isdigit, SERVER_PORT_STRING)))

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
                received_data, received_file_data = receive_data(client_socket)
                if received_data:
                    print("Received dictionary:", received_data)
                if received_file_data:
                    print("Received file data:", received_file_data)

    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")
