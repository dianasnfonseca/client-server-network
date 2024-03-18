import unittest
from unittest.mock import patch
from client import send_data
from serialization import serialize_to_json, serialize_to_xml, serialize_to_binary


print('testing client.py...')
class TestClient(unittest.TestCase):

    @patch('socket.socket')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="some_data")
    def test_send_data(self, mock_open, mock_socket):
        mock_socket.return_value.__enter__.return_value.recv.return_value = b'ack'
        data = {'name': 'Diana', 'group': 'D'}
        serialization_format = 'json'
        file_path = 'test_file.txt'
        encrypt_file = False
        send_data(data, serialization_format, file_path, encrypt_file)
        mock_open.assert_called_once_with('config/client_config.ini', 'rb')
        mock_socket.assert_called()

print('testing serialization.py...')
class TestSerialization(unittest.TestCase):

    def test_serialize_to_json(self):
        data = {'name': 'Alice', 'age': 30}
        expected_result = b'{"name": "Alice", "age": 30}'
        result = serialize_to_json(data)
        self.assertEqual(result, expected_result)

    def test_serialize_to_xml(self):
        data = {'name': 'Alice', 'age': 30}
        expected_result = b'<data><name>Alice</name><age>30</age></data>'
        result = serialize_to_xml(data)
        self.assertEqual(result, expected_result)

    def test_serialize_to_binary(self):
        data = {'name': 'Alice', 'age': 30}
        expected_result = b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x05Alice\x94\x8c\x03age\x94K\x1eub.'
        result = serialize_to_binary(data)
        self.assertEqual(result, expected_result)
