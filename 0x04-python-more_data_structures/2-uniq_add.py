#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for num in my_list:
        trial = my_list.count(num)
        print(trial)
        if trial > 1:
            i = 0
            index = my_list.index(num)
            while i != trial:
                my_list[index] = 0
                i += 1
    for num in my_list:
        result = result + num
    return result
