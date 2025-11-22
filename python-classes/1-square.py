#!/usr/bin/python3
"""Defines a square class with size validation."""
class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): Size of the square (must be >= 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
