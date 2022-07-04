#!/usr/bin/python3

"""
class Rectangle - implements a rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """implements a rectancle"""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area"""
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
