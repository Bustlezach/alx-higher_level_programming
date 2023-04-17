#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa
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

    update_state = session.query(State).filter(State.id == '2').first()
    update_state.name = 'New Mexico'
    session.commit()
    session.close()
