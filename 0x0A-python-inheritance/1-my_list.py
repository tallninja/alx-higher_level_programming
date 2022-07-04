#!/usr/bin/python3

class MyList(list):
    """My List"""
    def print_sorted(self):
        print(sorted(self))
