#!/usr/bin/python3
"""5-text_indentation"""


def text_indentation(text):
    """text indentation"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    x = 0
    for i in text:
        if i is not ' ':
            x = 0
        if x is 0:
            print(i, end="")
        if i in '.:?':
            print("\n")
            x = 1
