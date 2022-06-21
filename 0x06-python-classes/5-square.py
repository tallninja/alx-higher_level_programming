#!/usr/bin/python3

"""
class Square - A class that defines a square
"""


class Square:
    """Class representing a square object"""
    def __init__(self, size=0):
        """Class constructor"""
        self.__size = size

    @property
    def size(self):
        """Getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
