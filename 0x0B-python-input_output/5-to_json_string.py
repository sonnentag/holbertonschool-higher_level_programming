#!/usr/bin/python3
"""5-to_json_string"""

import json


def to_json_string(my_obj):
    """to_json_string"""

    return (json.dumps(my_obj, sort_keys=True))
