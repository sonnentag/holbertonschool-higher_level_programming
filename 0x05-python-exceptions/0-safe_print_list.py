#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element in range(0, x):
            print("{:d}".format(my_list[element]), end="")
            count += 1
        print()
    except:
        print()
        return (count)
    return (count)
