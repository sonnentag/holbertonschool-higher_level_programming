#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle"""

        Rectangle.number_of_instances += 1
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width__ = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height__ = height

    @property
    def width(self):
        """width getter"""

        return self.__width__

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width__ = value

    @property
    def height(self):
        """height getter"""

        return self.__height__

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height__ = value

    def area(self):
        """return area"""

        return self.__width__ * self.__height__

    def perimeter(self):
        """return perimeter"""

        if self.__width__ is 0 or self.__height__ is 0:
            return 0
        return 2 * (self.__width__ + self.__height__)

    def __str__(self):
        """prepare rectangle in string format ready to print"""

        if self.__width__ is 0 or self.__height__ is 0:
            return ""
        rect = ""
        for a in range(self.__height__):
            for b in range(self.__width__):
                rect += str(self.print_symbol)
            if a is not self.__height__ - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """representation of rectangle for eval"""

        rect = "Rectangle({}, {})".format(self.__width__, self.__height__)
        return rect

    def __del__(self):
        """perform on deletion"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return bigger of 2 rectangls given"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """define square as rect"""

        return cls(size, size)