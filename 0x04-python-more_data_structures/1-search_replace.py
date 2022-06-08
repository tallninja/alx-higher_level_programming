#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list and search and replace:
        copy = [val for val in my_list]
        for i in range(len(copy)):
            if copy[i] == search:
                copy[i] = replace
        return (copy)
