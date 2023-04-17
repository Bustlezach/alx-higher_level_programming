#!/usr/bin/python3
"""
This script prints the State object id
with the name passed as argument
from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")
