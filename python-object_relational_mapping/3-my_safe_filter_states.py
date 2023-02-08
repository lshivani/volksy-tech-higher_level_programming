#!/usr/bin/python3
""" sql injection"""


import sys
import MySQLdb

if __name__ == __main__:
    conn = MySQLdb.connect(host="localhost", port="3306", user="sys.argv[1]", passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name = {} ORDER BY id ASC".format(sys.argv[4])
            a = c.fetchall()
            for i in c:
                print()
            c.close()
            conn.close()
