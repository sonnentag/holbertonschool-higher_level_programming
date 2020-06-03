#!/usr/bin/python3
"""2-read_lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines"""

    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
            if nb_lines is 1:
                break
            nb_lines -= 1
