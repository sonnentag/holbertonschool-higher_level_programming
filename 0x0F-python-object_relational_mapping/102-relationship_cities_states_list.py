#!/usr/bin/python3
""" lists all cities by state """

from sys import argv
from model_state import Base, State
from model_city import City
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

    for c, s in sess.query(City, State).filter(City.state_id == State.id)\
                                       .order_by(City.id).all():
        print("{}: {} -> {}".format(c.id, c.name, s.name))

    sess.close()
