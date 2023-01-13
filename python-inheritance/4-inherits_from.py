#!/usr/bin/python3
""" inherits_from function"""


def inherits_from(obj, a_class):
    """ True or False """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
