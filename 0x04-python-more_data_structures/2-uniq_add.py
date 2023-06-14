#!/usr/bin/python3
def uniq_add(my_list=[]):
    
    v = 0

    set_list = set(my_list)
    for num in set_list:
        v += num
    return v
