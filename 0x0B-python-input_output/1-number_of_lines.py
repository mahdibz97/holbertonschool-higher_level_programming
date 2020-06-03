#!/usr/bin/python3
"""Define class"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, mode='r', encoding='UTF8') as f:
        num = 0
        for line in f:
            num += 1
    return num
