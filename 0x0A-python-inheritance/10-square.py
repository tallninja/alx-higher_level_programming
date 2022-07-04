#!/usr/bin/python3

"""
class Square - implements a square from a rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """implements a square from a rectangle"""
    
    def __init__(self, size):
        """constructor"""
        super().__init__(size, size)
        self.__size = size
