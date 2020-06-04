#!/usr/bin/python3
"""100-append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after"""

    with open(filename, "r") as in_file:
        temp = in_file.readlines()

    with open(filename, "w") as out_file:
        for line in temp:
            if search_string in line:
                line = line + new_string
            out_file.write(line)
