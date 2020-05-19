#!/usr/bin/python3
""" define a class Square """


class Square:
    """ class square """
    def __init__(self, size=0):
        """ square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ property """
        return self.__size

    @size.setter
    def size(self, value):
        """ size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ area """
        return self.__size ** 2
