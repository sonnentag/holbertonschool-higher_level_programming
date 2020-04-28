#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number is 0:
    print("{} is 0".format(number))

elif number > 0:
    print("{} is greater than 0".format(number))

else:
    print("{} is less than 0".format(number))
