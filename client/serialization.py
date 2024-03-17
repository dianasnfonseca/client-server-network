import pickle
import json
import xml.etree.ElementTree as ET

def serialize_data(data, format='json'):
    """
    Serialize data into the specified format.

    Args:
        data: Dictionary containing data to be serialized.
        format (str): Serialization format ('json', 'xml', or 'binary'). Defaults to 'json'.

    Returns:
        bytes: Serialized data in bytes format.
    """
    try:
        if format == 'json':
            return json.dumps(data).encode('utf-8')
        elif format == 'xml':
            root = ET.Element("data")
            for key, value in data.items():
                ET.SubElement(root, key).text = str(value)
            return ET.tostring(root)
        elif format == 'binary':
            return pickle.dumps(data)
        else:
            raise ValueError("Invalid serialization format.")
    except Exception as e:
        print(f"Serialization error: {e}")
        return None