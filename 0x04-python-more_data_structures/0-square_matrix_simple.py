#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        return ([[val ** 2 for val in row] for row in matrix])
