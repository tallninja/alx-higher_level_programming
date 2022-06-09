#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        return (
                sum(map(lambda x: x[0] * x[1], my_list)) /
                sum([val[1] for val in my_list])
        )
    return (0)
