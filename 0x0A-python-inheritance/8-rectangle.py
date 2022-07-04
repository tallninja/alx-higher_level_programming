#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
class Rectangle - implements a rectangle
"""


class Rectangle(BaseGeometry):
    """implements a rectancle"""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("hight", height)
        self.__width = width
        self.__height = height
