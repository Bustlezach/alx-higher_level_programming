#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == 0:
        return 0

    numerator = 0
    denominator = 0
    for i in my_list:
        numerator += i[0] * i[1]
        denominator += i[1]
    WA = numerator / denominator

    return WA
