#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    """A simple rectangle class"""
    def __init__(self, width=0, height=0):
        """
        This contructor initializer,
        have width and height default value of zero
        for objects of this class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This method makes width private and behaves as the getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter to capture a new value for width"""
        if not isinstance(value, int)
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int)
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the value of the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the value of the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Return a format of eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Displays a message whenever an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
