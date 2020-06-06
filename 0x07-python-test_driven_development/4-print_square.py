#!/usr/bin/python3
"""4-print_square"""


def print_square(size):
    """print_square"""

    line = ""
    c = 0

    if (type(size) is not int) or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    while c < size:
        line += "#"
        c += 1

    while c > 0:
        print(line)
        c -= 1
