#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """ reads the file and prints """
    with open(filename, encoding='utf-8')as file:
        for line in file:
            print(line, end="")
