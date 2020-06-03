#!/usr/bin/python3
"""4-append_write"""


def append_write(filename="", text=""):
    """append_write"""

    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(text))
