#!/usr/bin/python3
"""rectangle module"""


from models.base import Base

class Rectangle(Base):
"""Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
    """init rectangle"""

        self.__x = x
        self.__y = y
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return area"""

        return self.__width * self.__height

    def display(self):
        """print rectangle"""

        if self.__width is 0 or self.__height is 0:
            return ""
        rect = ""
        for a in range(self.__height):
            for b in range(self.__width):
                rect += "#"
            if a is not self.__height - 1:
                rect += "\n"
        print(rect)

    def __str__(self):
        """return object as printable string"""
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height))


    def update(self, *args, **kwargs):
        """update a variable number of attributes"""
        if len(args):
            for k, v in zip(['id', 'width', 'height', 'x', 'y'], args):
                setattr(self, k, v)
        else:
            for k in ['id', 'width', 'height', 'x', 'y']:
                if k in kwargs:
                    setattr(self, k, kwargs[k])
