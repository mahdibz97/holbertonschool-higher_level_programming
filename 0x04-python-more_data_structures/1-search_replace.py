#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(my_list) - 1):
        if i == search:
            new_list[i - 1] = replace
    return(new_list)
