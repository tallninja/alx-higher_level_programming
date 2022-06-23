#!/usr/bin/python3

def print_square(size):
    """
    prints a square with the character #
    size is the size length of the square
    size must be an integer and grater than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
