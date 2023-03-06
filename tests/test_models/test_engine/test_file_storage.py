"""Unittests for FileStorage module."""
import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import *


class TestFileStorage(unittest.TestCase):
    """Test FileStorage."""

    def setUp(self):
        self.store = FileStorage()

        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = BaseModel(test_args)

        self.test_len = 0
        if os.path.isfile("file.json"):
            self.test_len = len(self.store.all())

    def tearDown(self):
        if os.path.isfile("file.json"):
            os.remove('file.json')

    def test_all(self):
        """Test all modules."""
        self.assertEqual(len(self.store.all()), self.test_len)

    def test_new(self):
        """Test creation."""
        self.assertEqual(len(self.store.all()), self.test_len)
        self.model.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

    def test_save(self):
        """Test storage."""
        self.test_len = len(self.store.all())
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        b = User()
        self.assertNotEqual(len(self.store.all()), self.test_len + 2)
        b.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

    def test_reload(self):
        """Test refreshing."""
        pass


if __name__ == "__main__":
    unittest.main()
