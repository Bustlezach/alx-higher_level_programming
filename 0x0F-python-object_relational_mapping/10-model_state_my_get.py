#!/usr/bin/python3
"""
This script screens out all State objects with the name passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) != 5:
        print(f"Usage: {arguments[0]} username password db_name state_name")
        exit(1)

    username = arguments[1]
    password = arguments[2]
    data = arguments[3]
    state_name = arguments[4]

    # Connect to the database and get a state from the database.
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{data}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state is None:
        print('Not found')
    else:
        print(f"{state.id}")
