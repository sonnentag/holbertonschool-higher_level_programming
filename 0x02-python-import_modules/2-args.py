#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    if ac is 2:
        a_var = "argument"
    else:
        a_var = "arguments"
    if ac > 1:
        print("{} {}:".format(ac-1, a_var))
        x = 1
        while x < ac:
            print("{}: {}".format(x, argv[x]))
            x += 1
    else:
        print("0 {}.".format(a_var))
