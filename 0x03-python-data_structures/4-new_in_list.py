#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = [num for num in my_list]
    if idx < 0:
        return copy
    if idx >= len(copy):
        return copy
    copy[idx] = element
    return (copy)
