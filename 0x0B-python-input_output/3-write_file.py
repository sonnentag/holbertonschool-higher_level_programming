#!/usr/bin/python3
"""3-write_file"""


def write_file(filename="", text=""):
    """write_file"""

    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(text))
