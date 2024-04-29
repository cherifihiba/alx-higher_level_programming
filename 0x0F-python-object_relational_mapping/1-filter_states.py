#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve all states starting with 'N' sorted by id
    c.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' COLLATE utf8_bin ORDER BY `id`")

    # Fetch all rows and print the states
    for state in c.fetchall():
        print(state)
