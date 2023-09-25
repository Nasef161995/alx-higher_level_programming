#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    c = 0
    for a in my_list:
        c += 1

    for num in my_list:
        try:
            if type(num) != int:
                continue
            if i <= x - 1:
                print("{:d}".format(num), end='')
                i += 1
            if x > c:
                print(my_list[x])

        except Exception as error:

            print(type(error).__name__)

    print()
    return i
