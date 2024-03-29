#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    database = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         password=password, db=database, port=3306)
    cursor = db.cursor()
    num_rows = cursor.execute("SELECT cities.id, cities.name, states.name\
                           FROM cities INNER JOIN states\
                           ON cities.state_id=states.id\
                           ORDER BY cities.id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
