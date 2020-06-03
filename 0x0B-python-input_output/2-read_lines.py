#!/usr/bin/python3
"""Define class"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and print it"""
    with open(filename, mode='r', encoding='UTF8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for r in range(nb_lines):
                print(f.readline(), end="")
