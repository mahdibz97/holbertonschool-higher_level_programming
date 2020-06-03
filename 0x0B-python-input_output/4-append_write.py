#!/usr/bin/python3
"""Define class"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, mode='a', encoding='UTF8') as f:
        app = f.write(text)
    return app
