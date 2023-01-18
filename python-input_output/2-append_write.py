#!/usr/bin/python3
""" append write """


def append_write(filename="", text=""):
    """ no of characters """
    with open(filename, 'a', encoding='utf-8')as file:
        return file.write(text)
