#!/usr/bin/python3

"""
returns True if the object is exactly
an instance of the specified class
otherwise returns False
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an
    instance of the specified class
    otherwise False
    """
    return type(obj).__name__ == a_class.__name__
