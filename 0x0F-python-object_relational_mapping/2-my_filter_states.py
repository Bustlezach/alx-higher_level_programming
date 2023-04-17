#!/usr/bin/python3

"""
This script accesses a MySQL database and retrieves states in the argument.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    """Establish a connection to the MySQL database"""
    db_conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    """Create a cursor object and execute a query to retrieve all states"""
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC", (sys.argv[4],))
    state_rows = cursor.fetchall()

    """Loop through each row and print it to the console"""
    for state in state_rows:
        print(state)
