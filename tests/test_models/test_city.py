#!/usr/bin/python3

"""Unittest for Amenity Class."""

import unittest

from models.city import City

from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases City class."""

    def test_instance(self):
        """test instance."""
        city = City()
        self.assertIsInstance(city, City)

    def test_is_class(self):
        """test instance."""
        city = City()
        self.assertEqual(str(type(city)),
                         "<class 'models.city.City'>")

    def test_is_subclass(self):
        """test is_subclass."""
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))


if __name__ == "__main__":
    unittest.main()
