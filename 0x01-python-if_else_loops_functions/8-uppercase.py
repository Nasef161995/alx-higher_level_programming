#!/usr/bin/python3
def uppercase(str):
    for a in str:
        i = ord(a)
        if i >= 97 and i <= 122:
            print("{:c}".format(i-32), end="")
        else:
            print("{:c}".format(i), end="")
    print()
