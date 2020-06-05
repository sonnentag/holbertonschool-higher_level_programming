#!/usr/bin/python3
"""2-matrix_divided"""


def matrix_divided(matrix, div):
    """matrix divided"""

    mtrx = []
    x = 0

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    for row in matrix:
        rowx = []
        if x != 0:
            if x != len(row):
                raise TypeError(
                    "Each row of the matrix must have the same size")
        else:
            x = len(row)

        for i in row:
            if (not isinstance(i, int) and not isinstance(i, float)):
                raise TypeError(
                    "matrix must be a matrix" +
                    " (list of lists) of integers/floats")
            rowx.append(round((i / div), 2))

        mtrx.append(rowx)

    return (mtrx)
