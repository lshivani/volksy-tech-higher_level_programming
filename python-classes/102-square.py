#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """ square 8 """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        return(self.area() == other.area())

    def __ne__(self, other):
        return(self.area() != other.area())

    def __lt__(self, other):
        return(self.area() < other.area())

    def __le__(self, other):
        return(self.area() <= other.area())

    def __gt__(self, other):
        return(self.area() > other.area())

    def __ge__(self, other):
        return(self.area() >= other.area())
