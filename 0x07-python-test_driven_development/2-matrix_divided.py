#!/usr/bin/python3

"""
Contains matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix by divisor
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    m_len = 0
    if len(matrix) and isinstance(matrix[0], list):
        m_len = len(matrix[0])

    n_matrix = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if m_len != len(i):
            raise TypeError("Each row of the matrix must have the same size")

        i_matrix = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            i_matrix.append(round(j / div, 2))
        n_matrix.append(i_matrix)

    return n_matrix
