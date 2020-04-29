#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 15 is 0:
            print("FizzBuzz", end=" ")
        elif x % 3 is 0:
            print("Fizz", end=" ")
        elif x % 5 is 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(x), end=" ")
