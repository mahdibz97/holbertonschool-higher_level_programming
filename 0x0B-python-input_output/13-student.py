#!/usr/bin/python3
"""Define class"""


class Student:
    """defines a student by first_name last_name age"""
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

    def reload_from_json(self, json):
        """relode"""
        for i in json:
            self.__dict__[i] = json[i]
