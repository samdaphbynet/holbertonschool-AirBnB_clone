#!/usr/bin/python3
"""FileStorage class"""
import json
from os import path


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            new_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'W') as file:
            data = {}
            data.update(FileStorage.__objects)
            for key, value in data.items():
                data[key] = value.to_dict()
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
                }

        try:
            data = {}
            with open(FileStorage.__file_path, 'r') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        self.all[key] = classes(value['__class__'])(**value)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Deletes an object or all objects of a certain class."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if self.__objects[key]:
                del FileStorage.__objects[key]
                self.save()
    
    def close(self):
        # `self.reload()` is a method that deserializes
        # the JSON file to the `__objects` dictionary.
        self.reload()
