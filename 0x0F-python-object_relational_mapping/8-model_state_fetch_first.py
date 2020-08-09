#!/usr/bin/python3
""" prints the first State object """

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ main """

    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(db_user, db_pass, db_name)

    Session = sessionmaker(bind=create_engine(db))

    sess = Session()

    res = sess.query(State).first()

    print("{}: {}".format(res.id, res.name) if res else "Nothing")

    sess.close()
