#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return (None)
