#!/usr/bin/python3
"""This modle creates a class named Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square"""
    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns informal string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
