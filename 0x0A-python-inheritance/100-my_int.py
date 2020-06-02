#!/usr/bin/python3
""" Define my class """


class MyInt(int):
    """class MyInt"""

    def __ne__(self, other):
        """ne"""
        return int(self) == int(other)

    def __eq__(self, other):
        """rq"""
        return int(self) != int(other)
