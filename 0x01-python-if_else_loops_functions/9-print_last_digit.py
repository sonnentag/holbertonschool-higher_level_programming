#!/usr/bin/python3
def print_last_digit(n):
    x = abs(n) % 10
    print('{:d}'.format(x), end='')
    return (x)
