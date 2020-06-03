#!/usr/bin/python3
"""Define class"""


import json


def from_json_string(my_str):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding='UTF8') as f:
        my_str = json.dumps(my_obj)
        f.write(my_str)
