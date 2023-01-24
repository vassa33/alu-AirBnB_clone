#!/usr/bin/python3


"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel ."""

    def test_instance(self):
        """test instance."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_is_class(self):
        """test instance."""
        base = BaseModel()
        self.assertEqual(str(type(base)),
                         "<class 'models.base_model.BaseModel'>")


if __name__ == "__main__":
    unittest.main()
