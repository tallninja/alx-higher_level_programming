#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    copy = []
    for i in range(len(matrix)):
        copy.append([])
        for j in range(len(matrix[i])):
            copy[i].append(matrix[i][j] ** 2)
    return (copy)
