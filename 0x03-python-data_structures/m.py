#!/usr/bin/python3
my_list = [0, 1, 2, 3, 4, 5, 6]

list_result = []
for i in my_list:
    if i % 2 == 0:
        list_result.append(True)
    else:
        list_result.append(False)
    
print(list_result)
print(len(list_result))
