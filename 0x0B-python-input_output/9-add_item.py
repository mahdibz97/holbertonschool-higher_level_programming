#!/usr/bin/python3

"""A script that adds all arguments to a Python list, and then save them
to a file."""

from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    new = load(filename)
except:
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write('')
        new = []
if len(os.sys.argv) == 1:
    save(new, filename)
else:
    for i in range(1, len(os.sys.argv)):
        new.append(os.sys.argv[i])
    save(new, filename)