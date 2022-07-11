#!/usr/bin/python3
"""
models/base.py - Base
"""
import os
import json
import csv
import turtle
import time
from random import randrange


class Base:
    """will be the base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None and type(id) is not int:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
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
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()
            dict_list = cls.from_json_string(data)
            for item in dict_list:
                instances.append(cls.create(**item))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format and saves it to a file"""
        if (type(list_objs) is not list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""
        filename = f"{cls.__name__}.csv"
        obj_list = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        obj_list.append(i)
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle window and draws rectangles and squares"""
        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("white")
        t.shape("circle")
        t.pensize(4)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangleor Square"""
        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
