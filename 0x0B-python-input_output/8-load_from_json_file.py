#!/usr/bin/python3
"""Define class"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, mode='r', encoding='UTF8') as f:
        read = f.read()
        return json.loads(read)
