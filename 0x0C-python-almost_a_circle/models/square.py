#!/usr/bin/python3
"""
models/square.py - Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square from a rectangle"""

    def __init__(self, size, x=0, y=0):
        """constructor"""
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y)

    @property
    def size(self):
        """size getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"
