#!/usr/bin/python3
""" lists all states from a database providing connection info as args"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    state = argv[4]

    db = MySQLdb.connect("localhost", db_user, db_pass, db_name)

    cur = db.cursor()

    sql = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"

    cur.execute(sql, (state, ))

    for row in cur.fetchall():
        print(row)
