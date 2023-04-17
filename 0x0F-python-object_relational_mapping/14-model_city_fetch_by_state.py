#!/usr/bin/python3
"""
This script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password db_name state_name")
        exit(1)

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(City, State).join(State)

    for city, state in Query.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
