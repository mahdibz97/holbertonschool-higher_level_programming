#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new = []
        for j in range(len(matrix[i])):
            new.append(matrix[i][j] ** 2)
        new_matrix.append(new)
    return (new_matrix)
