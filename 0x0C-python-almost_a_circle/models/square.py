#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        self.__size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""

        if Rectangle.width.__get__(self) == Rectangle.height.__get__(self):
            return Rectangle.width.__get__(self)

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            self.__height = value
            self.__size = value

    def __str__(self):
        """return object as printable string"""

        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x, self.y, self.__size))

    def update(self, *args, **kwargs):
        """update a variable number of attributes"""
        if len(args):
            for k, v in zip(['id', 'size', 'x', 'y'], args):
                setattr(self, k, v)
        else:
            for k in ['id', 'size', 'x', 'y']:
                if k in kwargs:
                    setattr(self, k, kwargs[k])
