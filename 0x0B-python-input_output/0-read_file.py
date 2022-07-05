#!/usr/bin/python3
"""
read_file - reads the contents of a text file
"""


def read_file(filename=""):
    """reads the contents of a file"""
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
        print("{:s}".format(contents), end="")
