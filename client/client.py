import socket
import json  # Import JSON module for serialization
import configparser

def serialize_data(data):
    """
    Serialize data (dictionary) to JSON string.

    Args:
        data: Data (dictionary) to be serialized.

    Returns:
        str: Serialized data (JSON string).
    """
    return json.dumps(data)

def send_data(data):
    """
    Send serialized data to the server.

    Args:
        data: Data (dictionary) to be sent to the server.

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
            # Connect to server
            client_socket.connect((SERVER_IP, SERVER_PORT))

            # Serialize data (dictionary to JSON string)
            serialized_data = serialize_data(data)

            # Send serialized data to server
            client_socket.sendall(serialized_data.encode())
            print("Data sent successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Sample data to send
    data = {'name': 'Diana', 'role': 'SD & tester'}
    send_data(data)
