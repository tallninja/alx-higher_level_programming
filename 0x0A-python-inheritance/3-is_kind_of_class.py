#!/usr/bin/python3

"""
returns True if the object is an instance of,
or if the object is an instance of a class
that inherited from, the specified class
otherwise returns False
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of
    or if the object is an instance of a class that inherited from
    the specified class otherwise returns False
    """
    return isinstance(obj, a_class)
