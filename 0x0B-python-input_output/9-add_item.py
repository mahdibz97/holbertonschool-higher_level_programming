#!/usr/bin/python3
"""DEfine class"""


import os
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    new = load_from_json_file(filename)
finally:
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write('')
        new = []
if len(os.sys.argv) == 1:
    save_to_json_file(new, filename)
else:
    for i in range(1, len(os.sys.argv)):
        new.append(os.sys.argv[i])
    save_to_json_file(new, filename)
