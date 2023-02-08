#!/usr/bin/python3
""" cities name """

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT cities.name from cities" +
              " INNER JOIN states ON cities.state_id = state.id" +
              " WHERE states.name = %s ORDER BY cities.id ASC",
              [sys.argv[4]])
    a = c.fetchall()
    for i in a:
        print(",",join.[0])
    c.close()
    conn.close()
