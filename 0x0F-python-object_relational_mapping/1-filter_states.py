#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3])

    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

