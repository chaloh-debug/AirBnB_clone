#!/usr/bin/python3
"""This module contains a base class called 'FileStorage' that defines
the process that serializes and deserializes to JSON
file_storage module manages data stored in file.json
and manages CRUD operation
"""
import json
import os
import re


class FileStorage:
    """ An abstracted file storage engine
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
        class name.id
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with
        key <obj class name>.id save(self): serializes
        __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists otherwise
        , do nothing.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new instance of a specific class and
        saves it into the file storage
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the instances of all classes into a
        .json file using the json string format
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
