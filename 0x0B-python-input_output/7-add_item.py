#!/usr/bin/python3
"""
7-add_item.py - add_item
"""
import sys


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

def main():
    """adds all command line arguments to a list
    and save them to a file"""
    filename = "add_item.json"
    contents = []

    try:
        contents = load(filename)
    except FileNotFoundError as e:
        save(contents, filename)

    contents += sys.argv[1:]
    save(contents, filename)


if __name__ == "__main__":
    main()
