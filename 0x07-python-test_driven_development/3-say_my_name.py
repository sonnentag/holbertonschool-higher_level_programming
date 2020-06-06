#!/usr/bin/python3
"""3-say_my_name"""


def say_my_name(first_name, last_name=""):
    """say_my_name"""

    n = "first_name"
    x = 0

    for i in [first_name, last_name]:
        if not isinstance(i, str) or not first_name:
            if x == 1:
                n = "last_name"
            raise TypeError("{} must be a string".format(n))
        x = 1
    if x == 1:
        return
    else:
        for i in [first_name, last_name]:
            if x == 0:
                print("My name is {} ".format(i), end="")
            else:
                print("{}".format(i), end="")
            x = 1
    print()
