#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_conn = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_conn)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='California')
    san_francisco_city = City(name='San Francisco')
    cal_state.cities.append(san_francisco_city)

    session.add(cal_state)
    session.commit()
    session.close()
