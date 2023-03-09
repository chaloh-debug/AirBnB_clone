#!/usr/bin/python3
"""Class that serializes instances to JSON file and vice versa """
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes and deserializes JSON objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns __objeects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**0))
        except FileNotFoundError:
            pass
