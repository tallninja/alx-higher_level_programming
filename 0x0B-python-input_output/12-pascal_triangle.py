#!/usr/bin/python3
"""
12-pascal_triangle.py - pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of ints representing Pascals triangle"""
    if n <= 0:
        return []

    triangle = [[0 for x in range(i + 1)] for i in range(n)]
    triangle[0] = [1]

    for i in range(1, n):
        triangle[i][0] = 1
        for j in range(1, i + 1):
            if j < len(triangle[i - 1]):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            else:
                triangle[i][j] = triangle[i - 1][0]
    return triangle
