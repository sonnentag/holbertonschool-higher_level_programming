#!/usr/bin/python3
"""save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""

    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
