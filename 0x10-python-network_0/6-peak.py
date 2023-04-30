#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """
    :param list_of_integers: list containing integers
    :return: peak from list_of_integers or None
    """
    if len(list_of_integers) == 0:
        return None
    check = 0
    i = 0
    while i < len(list_of_integers):
        if check < list_of_integers[i]:
            check = list_of_integers[i]
        i += 1
    return check
