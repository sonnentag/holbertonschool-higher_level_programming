#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    op_d = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argv) is 4 and argv[2] in list(op_d):
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {}".format(a, argv[2], b, op_d[argv[2]](a, b)))
    elif len(argv) is 4:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
