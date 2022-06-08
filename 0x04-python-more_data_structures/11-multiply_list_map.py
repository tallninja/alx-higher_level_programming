#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    if my_list and number:
        return (list(map(lambda val: val * number, my_list)))
