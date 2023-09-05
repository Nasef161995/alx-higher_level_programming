#!/usr/bin/python3
def uppercase(str):
    for a in str:
        i = ord(a)
        if i >= 65 and i <= 90:
            print(chr(i), end="")
        elif i >= 97 and i <= 122:
            print(chr(i - 32), end="")
        else:
            print(chr(i), end="")
    print()
