import json
import xml.etree.ElementTree as ET
import pickle

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
            serialized_data = serialize_to_json(data)
        elif format == 'xml':
            serialized_data = serialize_to_xml(data)
        elif format == 'binary':
            serialized_data = serialize_to_binary(data)
        else:
            raise ValueError("Invalid serialization format.")
        
        return serialized_data
    except Exception as e:
        print(f"Serialization error: {e}")
        return None

def serialize_to_json(data):
    """
    Serialize data to JSON format.

    Args:
        data: Dictionary containing data to be serialized.

    Returns:
        bytes: Serialized data in JSON format.
    """
    try:
        serialized_data = json.dumps(data).encode('utf-8')
        print("Data serialized to JSON format:", serialized_data)
        return serialized_data
    except Exception as e:
        raise ValueError(f"JSON serialization error: {e}")

def serialize_to_xml(data):
    """
    Serialize data to XML format.

    Args:
        data: Dictionary containing data to be serialized.

    Returns:
        bytes: Serialized data in XML format.
    """
    try:
        root = ET.Element("data")
        for key, value in data.items():
            ET.SubElement(root, key).text = str(value)
        xml_data = ET.tostring(root)
        print("Data serialized to XML format:", xml_data)
        return xml_data
    except Exception as e:
        raise ValueError(f"XML serialization error: {e}")

def serialize_to_binary(data):
    """
    Serialize data to binary format using pickle.

    Args:
        data: Dictionary containing data to be serialized.

    Returns:
        bytes: Serialized data in binary format.
    """
    try:
        serialized_data = pickle.dumps(data)
        print("Data serialized to binary format:", serialized_data)
        return serialized_data
    except Exception as e:
        raise ValueError(f"Binary serialization error: {e}")
