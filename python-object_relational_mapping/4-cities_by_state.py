#!/bin/usr/python3
""" print cities """

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c =conn.cursor()
    c.execute("SELECT cities.id, cities.name, states.name from cities" +
            "INNER JOIN cities.states_id = states_id ORDER BY" +
            "cities_id ASC")
    a = c.fectchall()
    for i in a:
        print(i)
    c.close()
    conn.close()
