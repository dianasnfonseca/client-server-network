import socket
import configparser
from serialization import serialize_data

def send_data(data, serialization_format):
    """
    Send serialized data along with serialization format to the server.

    Args:
        data: Data (dictionary) to be sent to the server.
        serialization_format (str): Serialization format chosen by the user.

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
            print("Connected to server.")

            # Serialize data based on chosen format
            serialized_data = serialize_data(data, serialization_format)
            
            # Combine serialization format and length of serialized data
            message = f"{serialization_format} {len(serialized_data)}"
            client_socket.sendall(message.encode())
            print("Serialization format and length sent to server:", message)

            # Send serialized data to server
            client_socket.sendall(serialized_data)
            print("Serialized data sent to server.")

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

    # Send data with chosen format
    send_data(data, serialization_format)
