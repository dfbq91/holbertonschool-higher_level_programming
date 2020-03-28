#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa that
# match with user input (argv[4] avoiding SQL injection

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    command = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
    ORDER BY id ASC", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
