#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    elements = ""
    try:
        for i in range(x):
            elements += str(my_list[i])
            n += 1
    except Exception as e:
        pass
    finally:
        print("{}".format(elements))
        return (n)
