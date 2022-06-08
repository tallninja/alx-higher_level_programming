#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        return (list(set_1 - set_2) + list(set_2 - set_1))
