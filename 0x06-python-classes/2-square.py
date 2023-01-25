#!/usr/bin/python3
"""Define a class"""

class Square:
    """Class name is square"""

    def __init__(self, size=0):
        """Initialization of contractor args value to zero on default"""

        if not isinstance(size, int):
            """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
