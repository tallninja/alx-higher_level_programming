#!/usr/bin/python3
"""
models/base.py - Base
"""
import json


class Base:
    """will be the base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) < 0:
                f.write("[]")
            else:
                obj_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        obj_list = []
        if json_string is not None and json_string != "":
            if type(json_string) is not str:
                raise TypeError("json_string must be a string")
            obj_list = json.loads(json_string)
        return obj_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of base with all attributes already set"""
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy
     
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instances = []
        data = None
        filename = f"{cls.__name__}.json"
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        dict_list = cls.from_json_string(data)
        for item in dict_list:
            instances.append(cls.create(**item))
        return instances

