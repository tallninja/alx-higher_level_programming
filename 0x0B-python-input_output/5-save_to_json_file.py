#!/usr/bin/python3
"""
5-save_to_json_file.py - save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
