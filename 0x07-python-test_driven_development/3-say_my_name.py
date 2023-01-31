#!/usr/bin/python3

"""This module is a function that generates fullname."""

def say_my_name(first_name, last_name=""):
    """
    Function produces fullname of the user.
    Args:
        first_name(string): first argument
        last_name(string): second argument

    Raises:
        TypeError: first_name must be a string
                 : last_name must be a string

    Returns:
        No return value

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
