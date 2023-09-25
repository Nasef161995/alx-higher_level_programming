#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0 
    for num in my_list:
        try:
           
            if i <= x - 1:
                print("{:d}".format(num), end='')
                i += 1
            
        except (TypeError , ValueError) as error:
            continue
    print()
    return i
