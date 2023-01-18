#!/usr/bin/python3
""" write file"""


def number_of_lines(filename=""):
    """ lines count """
    count = 0
    with open(filename, encoding='utf-8')as file:
        for line in file:
            count =+ 1
    return count
