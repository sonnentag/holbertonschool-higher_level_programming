#!/usr/bin/python3
"""8-load_from_json_file"""

import json


def load_from_json_file(filename):
    """load_from_json_file"""

    with open(filename, encoding="utf-8") as myFile:
        return (json.loads(myFile.read()))
