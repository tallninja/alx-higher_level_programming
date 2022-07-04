#!/usr/bin/python3

"""
class MyInt - rebel class of int which has == and != inverted
"""


class MyInt(int):
    """rebel class of int"""

    def __eq__(self, int2):
        """returns True if self != int2 otherwise returns False"""
        return super().__ne__(int2)

    def __ne__(self, int2):
        """returns True if self == int2 otherwise returns False"""
        return super().__eq__(int2)
