#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """init doc"""
        self._Square__size = size

    @property
    def size(self):
        """size property doc"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter doc"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """area doc"""
        size = self.__size
        return size * size

    def my_print(self):
        """my_print doc"""
        size = self.__size

        if size == 0:
            print()

        for col in range(size):
            for row in range(size):
                print('#', end='')
            print()
