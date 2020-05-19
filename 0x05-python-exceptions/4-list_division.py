#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for c in range(list_length):
        new = 0
        try:
            new = (my_list_1[c] / my_list_2[c])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(new)
    return (new_list)
