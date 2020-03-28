#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
# that match with user input (argv[4].

import MySQLdb
from sys import argv


db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                     passwd=argv[2], db=argv[3])
cur = db.cursor()
m = "SELECT * FROM states WHERE name LIKE '{}'\
ORDER BY id ASC".format(argv[4])
cur.execute(m)
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
