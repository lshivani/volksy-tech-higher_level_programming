#!/usr/bin/python3
""" creates class name"""


class student:
    """class """


def __init__(self, first_name, last_name, age):
    """ initializing """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self):
    """ retruns data """
    return self.__dict__
