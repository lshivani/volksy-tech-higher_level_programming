#!/usr/bin/python3
def safe_print_interger(value):
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
