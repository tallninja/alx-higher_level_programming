#!/usr/bin/python3
"""
write_file - writes a string to a text file
"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    nb_characters = 0
    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
