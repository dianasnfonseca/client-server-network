import json
import xml.etree.ElementTree as ET
import pickle

def deserialize_data(data, format):
    """
    Deserialize data from the specified format.

    Args:
        data (bytes): Serialized data to be deserialized.
        format (str): Serialization format ('json', 'xml', or 'binary'). Defaults to 'binary'.

    Returns:
        dict: Deserialized data as a dictionary.
    """
    try:
        # Check the serialization format
        if format == 'json':
            # Deserialize JSON data
            deserialized_data = json.loads(data.decode('utf-8'))
        elif format == 'xml':
            # Parse XML data and convert it to dictionary
            root = ET.fromstring(data)
            deserialized_data = {elem.tag: elem.text for elem in root}
        elif format == 'binary':
            # Deserialize data using pickle
            deserialized_data = pickle.loads(data)
        else:
            # Invalid format
            raise ValueError("Invalid serialization format.")
        
        return deserialized_data
    except Exception as e:
        # Handle deserialization errors
        print(f"Deserialization error: {e}")
        return None
