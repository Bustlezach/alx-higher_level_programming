#!/usr/bin/python3

"""
This module contains the function which prints square with character
"""

def print_square(size):
    """
    A function that prints square with '#'.
    Args:
        size(int): length of square in integer

    Raises:
         TypeError: size must be an integer
         ValueError: size must be >= 0

    Returns: No return value

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    square = ""
    for col in range(size):
        square = '#' * size
        print(square)
