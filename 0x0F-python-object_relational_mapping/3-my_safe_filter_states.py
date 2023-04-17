#!/usr/bin/python3

"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    arguments = sys.argv
    if (len(arguments) != 5):
        print("Usage: {} <state_name>".format(sys.argv[0]))
        exit(1)
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
    cursor.execute("SELECT * FROM states WHERE states.name LIKE BINARY %s ORDER BY states.id;", (sys.argv[4],))
    state_rows = cursor.fetchall()

    """Loop through each row and print it to the console"""
    for state in state_rows:
        print(state)
