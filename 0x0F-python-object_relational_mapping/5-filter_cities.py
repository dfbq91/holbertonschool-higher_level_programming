#!/usr/bin/python3
# lists all cities from the database hbtn_0e_4_usa.

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
    ON cities.state_id=states.id WHERE states.name\
    LIKE BINARY %s ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    for i, row in enumerate(query_rows):
        if i == len(query_rows) - 1:
            print(row[0])
        else:
            print(row[0], end=', ')
    cur.close()
    db.close()
