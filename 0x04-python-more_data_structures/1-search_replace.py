#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    n = new.index(search)
    new.pop(n)
    new.insert(n, replace)
    return new
