#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for num in my_list:
        trial = my_list.count(num)
        if trial == 1:
            result = result + num
        else:
            i = 0
            result = result + num
            while i > trial:
                my_list[my_list.index(num)] = 0
                i += 1

    return result
