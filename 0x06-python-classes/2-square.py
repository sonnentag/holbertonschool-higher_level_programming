#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """init doc"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = _size
