#!/usr/bin/python3
""" lists all states from a database providing connection info as args"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user=argv[1]
    db_pass=argv[2]
    db_name=argv[3]

    db = MySQLdb.connect("localhost", db_user, db_pass, db_name)

    cursor = db.cursor()

    sql = 'SELECT id, name FROM states ORDER BY id ASC'

    cursor.execute(sql)

    for row in cursor.fetchall():
        print(row)
