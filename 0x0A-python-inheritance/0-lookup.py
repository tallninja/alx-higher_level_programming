#!/usr/bin/python3

def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return list(dir(obj))
