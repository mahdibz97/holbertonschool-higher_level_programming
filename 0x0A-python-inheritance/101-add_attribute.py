#!/usr/bin/python3
"""Define class"""


def add_attribute(obj, name, value):
    """add attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
