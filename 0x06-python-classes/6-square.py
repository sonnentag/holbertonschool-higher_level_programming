#!/usr/bin/python3
"""6-square module"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init square
        Args:
            size - size of square
            position - coordinates of a square        """

        self.size = size
        self.position = position

    @property
    def position(self):
        """position getter"""

        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""

        if not isinstance(value, tuple) or len(value) > 2:
            raise TypeError(
                'position must be a tuple of 2 positive integers')

        for i in 0, 1:
            if (type(value[i]) != int or value[i] < 0):
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
        self.__position = value

    @property
    def size(self):
        """size getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """area of square"""
        size = self.__size
        return (size * size)

    def my_print(self):
        """print square coordinates"""
        size = self.__size
        position = self.__position

        if size == 0:
            print()
            return

        for x in range(position[1]):
            print()
        for x in range(size):
                print(' ' * position[0], end='')
                print('#' * size)
