#!/usr/bin/python3

"""Sum up two values."""

def add_integer(a, b=98):
    """A documentation for add_integer function.

    Args:
        a(int): first variable
        b(int): second variable, with 98 as default value

    Raises:
        TypeError: If a or b are not integer or float numbers

    Returns:
        Summation of 'a' and 'b'

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
