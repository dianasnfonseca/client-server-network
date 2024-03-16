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
        # Check the serialization format
        if format == 'json':
            # Serialize data to JSON format
            serialized_data = json.dumps(data).encode('utf-8')
            return serialized_data
        elif format == 'xml':
            # Create XML element and add data as sub-elements
            root = ET.Element("data")
            for key, value in data.items():
                ET.SubElement(root, key).text = str(value)
            # Convert XML element tree to bytes
            xml_data = ET.tostring(root)
            return xml_data
        elif format == 'binary':
            # Serialize data using pickle
            # Note: You can replace this with your binary serialization method
            # serialized_data = pickle.dumps(data)
            serialized_data = bytes(str(data), 'utf-8')
            return serialized_data
        else:
            # Invalid format
            raise ValueError("Invalid serialization format.")
    except Exception as e:
        # Handle serialization errors
        print(f"Serialization error: {e}")
        return None