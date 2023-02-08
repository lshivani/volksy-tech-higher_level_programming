#!/usr/bin/python3
""" print cities """

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT cities.id, cities.name, states.name from cities" +
              " INNER JOIN states ON cities.state_id = states.id ORDER BY" +
              " cities.id ASC")
    a = c.fetchall()
    for i in a:
        print(i)
    c.close()
    conn.close()
