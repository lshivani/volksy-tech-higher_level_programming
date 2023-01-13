#!/usr/bin/python3
"class named MyList"


class MyList(list):
    """A class named MyList """
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
