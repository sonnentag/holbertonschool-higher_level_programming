#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 1
    a_sum = 0
    while x < len(argv):
        a_sum += int(argv[x])
        x += 1
    print("{}".format(a_sum))
