#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for v in my_list:
        if v == search:
            new_list.append(replace)
        else:
            new_list.append(v)
    return new_list
