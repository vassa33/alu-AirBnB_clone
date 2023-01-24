#!/usr/bin/python3

"""Unittest for User Class."""

import unittest

from models.user import User

from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases User class."""

    def test_instance(self):
        """test instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_is_class(self):
        """test instance."""
        user = User()
        self.assertEqual(str(type(user)),
                         "<class 'models.user.User'>")

    def test_is_subclass(self):
        """test is_subclass."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))


if __name__ == "__main__":
    unittest.main()
