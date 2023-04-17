#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    database = args[3]
    db_conn = MySQLdb.connect(host='localhost', user=username,
                         password=password, db=database, port=3306)
    cursor = db_conn.cursor()
    cursor.execute("SELECT cities.id, cities.name\
                           FROM cities\
                           JOIN states\
                           ON cities.state_id=states.id\
                           WHERE states.name LIKE BINARY '{}'\
                           ORDER BY cities.id ASC".format(args[4]))
    rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
    cursor.close()
    db_conn.close()
