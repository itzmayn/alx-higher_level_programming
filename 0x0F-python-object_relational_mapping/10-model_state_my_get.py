#!/usr/bin/python3

"""
A script that prints the State object with the name passed as an argument
from hbtn_0e_6_usa
Username, password, dbname, and name to search
will be passed as arguments to the script.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def print_state_id_by_name(username, password, database_name, state_name):
    try:
        # Create the database connection
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

        # Create a session
        with Session() as session:
            # Extract the state by name
            state = session.query(State).filter(State.name == state_name).one_or_none()

            # Print state ID
            if state is None:
                print("State not found")
            else:
                print("State ID:", state.id)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1:5]
    print_state_id_by_name(username, password, database_name, state_name)
