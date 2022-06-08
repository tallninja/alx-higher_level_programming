#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list and search and replace:
        copy = my_list.copy()
        for i in range(len(copy)):
            if copy[i] == search:
                copy[i] = replace
        return (copy)
