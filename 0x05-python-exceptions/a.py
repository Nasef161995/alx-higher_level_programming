#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        count+=1
    if x <= count:
        a = 0
        try:
            for num in my_list:
                if a <= x-1:
                    print(num, end='')
                    a+=1
        except:
            print('error')
        print()
        return x
    else:
        try:
            for n in my_list:
                print(n, end='')
        except:
            print('error')
        print()
        return count
