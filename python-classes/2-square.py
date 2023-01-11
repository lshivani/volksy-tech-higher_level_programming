#!/usr/bin/python3
""" 2-Square """


class Square:
    """ Size = 0 """
    def __init__(self, size = 0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            return ValueError("size must be >= 0")
        self.__size = size
