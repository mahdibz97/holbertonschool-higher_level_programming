#!/usr/bin/python3
"""Define class"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

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
        return self.__height * self.__width

    def perimeter(self):
        """perimetre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """str"""
        str = ""
        if self.height == 0 or self.width == 0:
            return str
        for i in range(self.height):
            for j in range(self.width):
                str += '#'
            if i != self.height - 1:
                str += '\n'
        return str

    def __repr__(self):
        """repr"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
    