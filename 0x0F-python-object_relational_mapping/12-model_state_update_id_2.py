#!/usr/bin/python3
""" update name of state with id 2 to New Mexico """

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

    sess.query(State).filter(State.id == '3').one().name = 'New Mexico'

    sess.commit()

    sess.close()
