#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = []
        for x in i:
            row.append(x ** 2)
        new_matrix.append(row)
    return new_matrix
