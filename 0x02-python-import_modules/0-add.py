#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    add_0 = __import__('add_0', globals(), locals(), 'add', 0)
    add = add_0.add
    print("{} + {} = {}".format(a, b, add(a, b)))