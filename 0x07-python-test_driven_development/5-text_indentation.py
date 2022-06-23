#!/usr/bin/python3

def text_indentation(text):
    """
    prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    string = ""
    for char in text:
        string += char
        if char in ".:?":
            string += "\n\n"

    string = "\n\n".join(string.split("\n\n "))
    print(string, end="")

