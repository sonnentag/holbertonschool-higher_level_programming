#!/usr/bin/python3
""" insert Lousiana into States table and print it's new id """

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ main """

    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]

    state = 'Lousiana'

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(db_user, db_pass, db_name)

    Session = sessionmaker(bind=create_engine(db))

    sess = Session()

    sess.add(State(name='state'))

    sess.commit()

    res = sess.query(State).filter(State.name == state)

    for row in res:
        print("{}".format(row.id))

    sess.close()
