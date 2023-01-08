#!/usr/bin/python3

new_string = ''
def no_c(my_string):
    for chr in my_string:
        if ((chr != 'C') and (chr != 'c')):
            new_string += chr

    return (new_string)
