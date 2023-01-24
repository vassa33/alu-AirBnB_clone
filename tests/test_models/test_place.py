#!/usr/bin/python3

"""Unittest for Place Class."""

import unittest

from models.place import Place

from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases Place class."""

    def test_instance(self):
        """test instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_is_class(self):
        """test instance."""
        place = Place()
        self.assertEqual(str(type(place)),
                         "<class 'models.place.Place'>")

    def test_is_subclass(self):
        """test is_subclass."""
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))


if __name__ == "__main__":
    unittest.main()
