def uppercase(str):
    for x in str:
        x = ord(x)
        if x > 96 and x < 123:
            x = x - 32
        print('{:c}'.format(x), end='')
    print()
