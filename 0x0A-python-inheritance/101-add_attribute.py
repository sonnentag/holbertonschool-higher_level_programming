#!/usr/bin/python3
"""101-add_attribute"""


def add_attribute(obj, name, value):
    """add_attribute"""

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new atribute")
