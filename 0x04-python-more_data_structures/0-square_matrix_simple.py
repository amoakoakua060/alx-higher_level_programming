#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list) and len(matrix):
        return [[a**2 for a in line] for line in matrix]
