#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for num in range(0, x):
        try:
            print(my_list[num], end='')
            i += 1
        except BaseException:
            x = x

    print()
    return i
