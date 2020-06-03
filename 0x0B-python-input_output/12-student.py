#!/usr/bin/python3
"""Define class"""


class Student:
    """class Student that defines a student by based on 11-student.py"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        _dict = {}
        if attrs is not None:
            for i in range(len(attrs)):
                if attrs[i] in self.__dict__:
                    _dict[attrs[i]] = self.__dict__[attrs[i]]
            return _dict
        return self.__dict__
