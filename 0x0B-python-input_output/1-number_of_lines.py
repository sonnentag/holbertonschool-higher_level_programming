#!/usr/bin/python3
"""1-number_of_lines"""


def number_of_lines(filename=""):
    """number_of_lines"""

    lines = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            lines += 1
    return (lines)
