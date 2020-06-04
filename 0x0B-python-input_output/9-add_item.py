#!/usr/bin/python3
"""add_item"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    loaded = load_from_json_file(filename)
except FileNotFoundError:
    loaded = []
loaded.extend(sys.argv[1:])
save_to_json_file(loaded, filename)
