import unittest
import sqlite3
from src.db.database import Database

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database(':memory:')  # Use an in-memory database for testing
        cls.db.create_table()  # Create the table for testing

    def test_add_client(self):
        client_id = 100
        name = "Test Client"
        self.db.add_client(client_id, name)
        client = self.db.get_client(client_id)
        self.assertEqual(client[0], client_id)
        self.assertEqual(client[1], name)

    def test_get_client_not_found(self):
        client = self.db.get_client(999)  # Non-existent client
        self.assertIsNone(client)

    def test_update_client(self):
        client_id = 100
        new_name = "Updated Client"
        self.db.update_client(client_id, new_name)
        client = self.db.get_client(client_id)
        self.assertEqual(client[1], new_name)

    def test_delete_client(self):
        client_id = 100
        self.db.delete_client(client_id)
        client = self.db.get_client(client_id)
        self.assertIsNone(client)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

if __name__ == '__main__':
    unittest.main()