#!/usr/bin/python3
"""
6-load_from_json_file.py - load_from_json_file
"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    obj = None
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
    return obj
