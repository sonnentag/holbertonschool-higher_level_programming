#!/usr/bin/python3
"""
0-add_integer
    a: int 1, b: int 2, return sum of a + b
tests in tests dir
"""


def add_integer(a, b=98):
    """add_integer - adds two integers
    a: int 1, b: int 2
    Return: sum of a and b"""
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')

    return (a) + (b)
