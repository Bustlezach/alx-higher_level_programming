#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) != 4:
        print(f"Usage: {arguments[0]} username password db_name")
        exit(1)

    username = arguments[1]
    password = arguments[2]
    data = arguments[3]

    # Connect to the database and get a state from the database.
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{data}")
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).first()

    if instance is None:
        print('Nothing')
    else:
        print(f"{instance.id}: {instance.name}")

