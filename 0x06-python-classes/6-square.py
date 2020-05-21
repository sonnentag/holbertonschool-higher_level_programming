#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init doc"""
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """size property doc"""
        return self.__position

    @position.setter
    def position(self, value):
        """size setter doc"""
        if not isinstance(value, tuple) or len(value) is not 2:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        for i in 0, 1:
            if type(value[i]) != int or value[i] < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            else:
                self.__position[i] = value

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
        position = self.__position

        if size == 0:
            print()
            return

        for x in range(position[1]):
            print()
        for x in range(size):
            for x in range(position[0]):
                print(' ', end='')
            for x in range(size):
                print('#', end='')
            print()
