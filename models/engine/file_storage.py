#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): Name of the file to save objects to.
        __objects (dict): Dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with the  key <obj_class_name>.id"""
        oclname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oclname, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize JSON file __file_path to __objects,that is if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cl_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cl_name)(**o))
        except FileNotFoundError:
            return
