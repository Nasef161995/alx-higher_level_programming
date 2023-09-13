#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    n = my_list.index(search)
    new[n] = replace
    return new

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)    
