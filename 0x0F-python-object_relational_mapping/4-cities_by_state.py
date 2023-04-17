#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves all cities and their corresponding state names,
and then prints them to the console.
"""

import MySQLdb
import sys

# Check if the command line arguments are valid
if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} username password database_name")
    sys.exit(1)

# Get the command line arguments for database credentials
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the database
try:
    db_conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        port=3306,
        db=database
    )
except MySQLdb.Error as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

# Create a cursor object and execute a query to retrieve all cities and their corresponding state names
try:
    cursor = db_conn.cursor()
    cursor.execute("SELECT states.name, cities.id, cities.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC")
    city_rows = cursor.fetchall()
except MySQLdb.Error as e:
    print(f"Error executing query: {e}")
    cursor.close()
    db_conn.close()
    sys.exit(1)

# Loop through each row and print it to the console
for city in city_rows:
    print(city)

# Close the cursor and database connection
cursor.close()
db_conn.close()

