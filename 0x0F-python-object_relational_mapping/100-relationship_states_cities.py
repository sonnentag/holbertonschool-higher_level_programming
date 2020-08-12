#!/usr/bin/python3
""" update name of state with id 2 to New Mexico """

from sys import argv
from relationship_state import Base, State
from sqlalchemy import create_engine, select, Table, MetaData
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == '__main__':
    """ main """

    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(db_user, db_pass, db_name)
    engine = create_engine(db)
    conn = engine.connect()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    sess = Session()

    ca = State(name='California')
    ca.cities = [City(name='San Francisco')]
    sess.add(ca)

    sess.commit()

    sess.close()
