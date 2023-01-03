#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ((ord(char) >= 97) and (ord(char) <= 121)):
            i = chr((ord(char) - 32))
            print("{}".format(i), end="")
        print()
