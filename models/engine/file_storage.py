#!/usr/bin/python3
"""
Module file_storage.py
Handles serialization and deserialization
of instances to and from json
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    private class attributes 
    __file_path: string
    __objects: dictionary
    public instance methids 
    all(self)
    new(self, obj)
    save(self)
    reload(self)
    """
    # Path to file where json will be stored
    __file_path = "file.json"
    # Stores all objects by <class name>.id
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj:
            # Create the key
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """serialize __objects to json"""
        obj_dict = {}

        # iterates through __objects
        # converts each objexts to a dictionary
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

            # open fil, serialize and wroite file
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                json.dump(obj_dict, f)

    def reload(self):
        """deserializes json file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                dict_objs = json.load(f)
            for obj in dict_objs.values():
                # pick the classname
                class_name = obj["__class__"]
                self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
        
                
