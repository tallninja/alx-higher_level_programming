#!/usr/bin/python3

"""
class Rectangle defines a rectangle
"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        return (2 * (self.__width + self.__height))

    def __str__(self):
        str_rep = ""
        for i in range(self.__height):
            str_rep += ("#" * self.__width)
            if i < self.__height - 1:
                str_rep += "\n"
        return (str_rep)

    def __repr__(self):
        return (f"{type(self)}({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
