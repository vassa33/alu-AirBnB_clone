#!/usr/bin/python3

"""Unittest for FileStorage Class."""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def test_instance(self):
        """test instance."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_is_class(self):
        """test instance."""
        storage = FileStorage()
        self.assertEqual(str(type(storage)),
                         "<class 'models.engine.file_storage.FileStorage'>")


if __name__ == "__main__":
    unittest.main()
