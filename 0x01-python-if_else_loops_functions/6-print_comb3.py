#!/usr/bin/python3
i1 = 0
i2 = 1

while i1 < 10:
    while i2 < 10:
        print("{:d}{:d}".format(i1, i2), end="")
        if i1 + 1 != 9 or i2 != 9:
            print(",", end=" ")

        i2 = i2 + 1

    i1 = i1 + 1
    i2 = i1 + 1

print()
