#!/usr/bin/python3
"""Define class"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, mode='r', encoding='UTF8') as f:
        for line in f:
            print(line, end="")
