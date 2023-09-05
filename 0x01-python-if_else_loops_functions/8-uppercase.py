#!/usr/bin/python3
def uppercase(str):
    for a in str:
        i = ord(a)
        if i >= 65 and i <= 90:
            print(f"{i:c}", end="")
        elif i >= 97 and i <= 122:
            print(f"{i-32:c}", end="")
        else:
            print(f"{i:c}", end="")
    print()
