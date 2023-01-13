#!/usr/bin/python3
""" class exception"""


class BaseGeometry:
    """ not implemented """
    def area(self):
        """ raise exception"""
        raise Exception("area() is not implemented")
