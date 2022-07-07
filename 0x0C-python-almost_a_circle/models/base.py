#!/usr/bin/python3
"""
models/base.py - Base
"""


class Base:
    """will be the base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
