#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init square"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""

        return (self.width)

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """return object as printable string"""

        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """update a variable number of attributes"""
        c = 0
        keys = ['id', 'size', 'x', 'y']
        if len(args):
            for v in args:
                if keys[c] == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, keys[c], v)
                c += 1
        else:
            for k in keys:
                if k in kwargs:
                    if k is 'size':
                        setattr(self, 'width', kwargs[k])
                        setattr(self, 'height', kwargs[k])
                    else:
                        setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """return square attributes as dict"""
        dictnry = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

        return (dictnry)
