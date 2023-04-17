#!/usr/bin/python3

"""
This script accesses a MySQL database and it truncates the result where necessary.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    """Establish a connection to the MySQL database"""
    db_conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        port=3306,
        db=database
    )

    """Create a cursor object and execute a query to retrieve all states"""
    cursor = db_conn.cursor()
    cursor.execute("SELECT states.name, cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    city_rows = cursor.fetchall()

    """Loop through each row and print it to the console"""
    for city in city_rows:
        print(city)
