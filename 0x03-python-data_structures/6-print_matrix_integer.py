#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            print("{:d} {:d} {:d}".format(row[0], row[1], row[2]))
        else:
            print()
