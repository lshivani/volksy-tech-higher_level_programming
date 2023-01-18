#!/usr/bin/python3
""" write file"""


def write_file(filename="", text=""):
    """ lines count """
    with open(filename,'w', encoding='utf-8')as file:
        return file.write(text)
