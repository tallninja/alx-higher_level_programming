#!/usr/bin/python3

"""
MyList inherits from list
print_sorted - that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """My List"""
    def print_sorted(self):
        print(sorted(self))
