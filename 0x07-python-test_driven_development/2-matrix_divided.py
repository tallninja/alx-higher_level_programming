#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    All elements of the matrix are be divided by div
    rounded to 2 decimal places
    Returns a new matrix
    """
    new_matrix = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for k in range(len(matrix[i])):
            el = matrix[i][k]
            if type(el) is not int and type(el) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i].append(round(el / div, 2))

    return (new_matrix)
