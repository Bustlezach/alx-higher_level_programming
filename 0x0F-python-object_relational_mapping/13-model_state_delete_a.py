#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password db_name state_name")
        exit(1)

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    for del_state in session.query(State).filter(State.name.contains('a')):
        session.delete(del_state)
    session.commit()
    session.close()
