import json
import xml.etree.ElementTree as ET
import pickle

def serialize_data(data, format):
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
            print("Data serialized to JSON format:", serialized_data)
            return serialized_data
        elif format == 'xml':
            # Create XML element and add data as sub-elements
            root = ET.Element("data")
            for key, value in data.items():
                ET.SubElement(root, key).text = str(value)
            # Convert XML element tree to bytes
            xml_data = ET.tostring(root)
            print("Data serialized to XML format:", xml_data)
            return xml_data
        elif format == 'binary':
            # Serialize data using pickle
            serialized_data = pickle.dumps(data)
            print("Data serialized to binary format:", serialized_data)
            return serialized_data
        else:
            # Invalid format
            raise ValueError("Invalid serialization format.")
    except Exception as e:
        # Handle serialization errors
        print(f"Serialization error: {e}")
        return None
