#!/usr/bin/python3
""" load file """


import json


def load_from_json_file(filename):
    """ load from json file"""
    with open(filename, encoding='utf-8')as file:
        return json.loads(file.read())
