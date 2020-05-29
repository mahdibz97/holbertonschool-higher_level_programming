#!/usr/bin/python3
"""Define class"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @width.setter
    def width(self, value):
        """width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.width * self.height

    def perimeter(self):
        """perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """str"""
        str = ""
        for i in range(self.height):
            for j in range(self.width):
                str += '#'
            str += '\n'
        return str

    def __repr__(self):
        """repr"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """del"""
        print("Bye rectangle...")
        del(self)
        Rectangle.number_of_instances -= 1
