#!/usr/bin/python3

def max_integer(my_list=[]):
    max_int = None

    if my_list != '':
        for i in my_list:
            if max_int < i:
                max_int = i
        return max_int

    else:
        return None
