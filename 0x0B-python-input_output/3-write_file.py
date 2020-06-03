#!/usr/bin/python3
"""Define classs"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, mode='w', encoding='UTF8') as f:
        w = f.write(text)
    return w
