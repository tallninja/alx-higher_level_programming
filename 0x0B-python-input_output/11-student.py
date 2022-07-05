#!/usr/bin/python3
"""
Student module
"""
import json


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        attrs_dict = {}
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for attr in attrs:
                if attr in self.__dict__:
                    attrs_dict.update({attr: self.__dict__[attr]})
            return attrs_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for attr in json:
            self.__dict__().update({attr: json[attr]})
