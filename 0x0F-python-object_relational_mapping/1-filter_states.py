#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves the states that match the given name, and prints them to the console.
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

