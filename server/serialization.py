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
        if format == 'json':
            return json.loads(data.decode('utf-8'))
        elif format == 'xml':
            root = ET.fromstring(data)
            return {elem.tag: elem.text for elem in root}
        else:
            return pickle.loads(data)
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None