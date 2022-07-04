#!/usr/bin/python3

"""
MyList inherits from list
print_sorted - that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """My List"""

    def print_sorted(self):
        """prints the list in ascending order"""
        copy = sorted(self[:])
        print(copy)

