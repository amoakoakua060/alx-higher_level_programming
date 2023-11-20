#!/usr/bin/python3

"""
this fetches cities which belongs to states with
a given name
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2],
            db=argv[3], host="localhost", port=3306)
    cur = db.cursor()

    cur.execute(
            """SELECT cities.name FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            WHERE states.name = %s ORDER BY cities.id ASC
            """, (argv[4], )
    )

    rows = cur.fetchall()
    rows = [row[0] for row in rows]
    print(*rows, sep=", ")

    cur.close()
    db.close()
