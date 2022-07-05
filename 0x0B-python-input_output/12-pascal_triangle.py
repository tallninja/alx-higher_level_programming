#!/usr/bin/python3
"""
12-pascal_triangle.py - pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of ints representing Pascals triangle"""
    if n <= 0:
        return []

    l = [[0 for x in range(i + 1)] for i in range(n)]
    l[0] = [1]

    for i in range(1, n):
        l[i][0] = 1
        for j in range(1, i + 1):
            if j < len(l[i - 1]):
                l[i][j] = l[i - 1][j - 1] + l[i - 1][j]
            else:
                l[i][j] = l[i - 1][0]
    return l
