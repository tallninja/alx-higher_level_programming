#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    print(dict(sorted(a_dictionary.items(), key = lambda x: x[0])))
