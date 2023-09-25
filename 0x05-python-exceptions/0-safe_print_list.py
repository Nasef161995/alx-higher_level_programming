#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for num in my_list:
        try:
            if i <= x - 1:
                print(num, end='')
                i += 1
        except BaseException:
            i = 1
            for n in my_list:
                print(n, end='')
                i += 1
            print()
            return i

    print()
    return i