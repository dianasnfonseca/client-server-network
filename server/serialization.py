import pickle
import json
import xml.etree.ElementTree as ET

def deserialize_data(data, format='json'):
    """
    Deserialize data from the specified format.

    Args:
        data (bytes): Serialized data to be deserialized.
        format (str): Serialization format ('json', 'xml', or 'pickle'). Defaults to 'json'.

    Returns:
        dict: Deserialized data as a dictionary.
    """
    try:
        # Check the serialization format
        if format == 'json':
            # Deserialize JSON data
            deserialized_data = json.loads(data.decode('utf-8'))
            return deserialized_data
        elif format == 'xml':
            # Parse XML data and convert it to dictionary
            root = ET.fromstring(data)
            deserialized_data = {elem.tag: elem.text for elem in root}
            return deserialized_data
        else:
            # Deserialize data using pickle (default)
            deserialized_data = pickle.loads(data)
            return deserialized_data
    except Exception as e:
        # Handle deserialization errors
        print(f"Deserialization error: {e}")
        return None
