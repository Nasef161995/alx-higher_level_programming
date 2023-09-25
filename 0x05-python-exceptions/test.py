#!/usr/bin/python3
a = [1,2,3,4,5]
n = 10
x = 0
for i in a:
    try:
        if x <= n-1: 
            print(i, end='')
            x+=1
    except:
        for i in a:
            print(i, end='')
print('--------------------')



def safe_print_list(my_list=[], x=0):
    i = 0
    for num in my_list:
        try:
            if i <= x-1:
                print(num, end='')
                i += 1
        except:
            i = 1
            for n in my_list:
                print(n, end='')
                i += 1
            print()
            return i
    else:
        print()
        return x
