#!/usr/bin/python3
"""
append_write - appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    nb_characters = 0
    with open(filename, "a", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
