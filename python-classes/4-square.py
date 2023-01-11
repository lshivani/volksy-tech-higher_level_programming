#!/usr/bin/python3
""" 4-square """


class Square:
    """ class """
    def __init__(self, size=0):
        self.__size = size

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            return ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size * self.__size

    def size(self):
        return self.__size
