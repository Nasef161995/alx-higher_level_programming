#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    n = my_list.index(search)
    new[n] = replace
    return new
