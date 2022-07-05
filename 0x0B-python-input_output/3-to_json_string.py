#!/usr/bin/python3
"""
to_json_tring - returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    return json.JSONEncoder().encode(my_obj)
