#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = float(a / b)
    except:
        x = 'None'
    finally:
        print("Inside result: {}".format(x))
    return (x)
