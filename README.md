# Project Readme: Client-Server Network

---

## Project Overview:
This project aims to establish a simple client-server network with specific functionalities. The requirements are outlined as follows:

## Project Requirements:
1. **Network Establishment:**
    - Build a simple client/server network.
  
2. **Tasks:**
    - **1.1) Dictionary Serialization:**
        - Create a dictionary, serialize it, and send it to the server.
    - **1.2) File Transmission:**
        - Create a text file and send it to the server.
    - **1.3) Serialization Format Selection:**
        - Allow the user to set the pickling format to binary, JSON, or XML.
    - **1.4) Text Encryption:**
        - Provide the option to encrypt the text in a file.
    - **1.5) Server Configuration:**
        - Allow the server to print sent items' contents to the screen and/or a file.
    - **1.6) Encryption Handling:**
        - Ensure the server can handle encrypted contents.
    - **1.7) Flexibility:**
        - Enable the client and server to operate on separate or the same machines.
    - **1.8) Code Standards:**
        - Adhere to PEP standard and utilize exception handling for error management.
    - **1.9) Unit Testing:**
        - Write unit tests to ensure functionality.

## Running the Project:
1. **Terminal Setup:**
    - Open a terminal.
2. **Server Execution:**
    - Navigate to the server directory.
    - Run `python server.py`.
3. **Client Execution:**
    - Open a new terminal window.
    - Navigate to the client directory.
    - Run `python client.py`.

## Example Output:
### Server Terminal:
```
Server is listening on 127.0.0.1:1072
Connection established with ('127.0.0.1', 53901)
Received data from the client: json 40
Serialization format received from the client: json
Received length data: 40
Length of serialized data: 40
Serialized data received from the client (40 bytes): b'{"name": "Diana", "group": "D"}'
Received dictionary: {"name": "Diana", "group": "D"}
Length of file data: 120
File data received from the client: b'gAAAAABl-IwhOySGHjYgYWECJDqhmhyCLEDds5mtEMTQZ-xYHTnBaUrMD01-Gz8wXQiQUfgh5WEuVdvIiq1AUfIcsnpWRdeQFs08fdPkWWOYZmKbFu_yWzc='
```

### Client Terminal:
```
Choose serialization format:
1. JSON
2. XML
3. Binary
Enter your choice (1/2/3): 1
Enter the file path to send (leave blank to skip): sample.txt
Encrypt file? (yes/no): yes
Data serialized to JSON format: b'{"name": "Diana", "group": "D"}'
```

---
This readme provides a comprehensive understanding of the project's objectives, steps for execution, and an example of expected outputs.
