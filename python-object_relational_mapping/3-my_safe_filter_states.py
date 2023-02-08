#!/usr/bin/python3
""" sql injection"""

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",[sys.argv[4]])
            a = c.fetchall()
            for i in a:
                print()
            c.close()
            conn.close()
