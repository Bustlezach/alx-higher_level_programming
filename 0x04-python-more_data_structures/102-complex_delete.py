#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    check = value
    
    new_dictionary = {}
    for key, value in a_dictionary.items():
        if value != check:
            return a_dictionary

        if value == check:
            del key
        else:
            new_dictionary[key] = value
    return new_dictionary
