#!/usr/bin/python3
# lists all City objects from the database hbtn_0e_14_usa
# using SQLAlchemy

import sys

from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # equivalent to select SQL expression
    for s, c in session.query(State, City).\
            filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
