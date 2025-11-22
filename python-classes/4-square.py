#!/usr/bin/python3
"""
Defines a square class with size validation, property,
area computation, and printing.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square (must be >= 0).
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): New size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #; empty line if size is 0."""
        if self.__size == 0:
            print()
            return

        for _ range(self.__size):
            print('#' * self.__size)
