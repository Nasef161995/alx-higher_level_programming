#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
n = my_list.index(5)
my_list[n] = 100000000
print(my_list)
