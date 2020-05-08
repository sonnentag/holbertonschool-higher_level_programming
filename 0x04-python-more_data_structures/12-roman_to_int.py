#!/usr/bin/python3
def roman_to_int(roman_string):
    r = 0
    p = 0
    x = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for c in reversed(roman_string):
        v = x[c]
        r += (v, -v)[v < p]
        p = v
    return (r)
