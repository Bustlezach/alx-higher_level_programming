#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            aa = 0,
            tuple_a = tuple_a + aa
        else:
            aa = (0, 0)
            tuple_a = tuple_a + aa


    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            bb = 0,
            tuple_b = tuple_b + bb
        else:
            bb = (0, 0)
            tuple_b = tuple_b + bb


    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]

    tuple_add = (a, b)
    return (tuple_add)
