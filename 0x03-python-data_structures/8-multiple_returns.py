#!/usr/bin/python3

def multiple_returns(sentence):
    
    length = len(sentence.strip())

    if length == 0:
        first = None
    else:
        first = sentence[0]
        
    str_tuple = (length, first)
    return str_tuple
