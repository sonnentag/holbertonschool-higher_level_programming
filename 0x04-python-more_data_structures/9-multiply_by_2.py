#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    anotha_dict = a_dictionary.copy()
    for i in anotha_dict:
        anotha_dict[i] = 2 * anotha_dict[i]
    return (anotha_dict)
