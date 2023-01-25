#!/usr/bin/python3
"""Define a class"""

class Square:
    """Class name is square"""

    def __init__(self, size=0):
        """Initialization of contractor args value to zero on default"""

        if not isinstance(size, int):
            """check if args exists in the class attribute"""

            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
