import socket
import configparser
from serialization import deserialize_data

def receive_data(client_socket):
    """
    Receive and process data from the client.

    Args:
        client_socket: Socket object for the client connection.

    Returns:
        None
    """
    try:
        # Receive serialization format and length of serialized data from the client
        format_length_data = client_socket.recv(1024).decode().strip()
        format_choice, length_data = format_length_data.split(" ")
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

    except Exception as e:
        print(f"Deserialization error: {e}")

if __name__ == "__main__":
    try:
        # Load server configuration
        config = configparser.ConfigParser()
        config.read('config/server_config.ini')

        # Create socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
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
                receive_data(client_socket)

    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")
