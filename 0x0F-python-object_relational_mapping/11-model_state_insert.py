#!/usr/bin/python3
"""
A script that adds the State object 'Louisiana' to hbtn_0e_6_usa
Username, password, dbname will be passed as arguments to the script.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def add_louisiana_state(username, password, database_name):
    try:
        # Create the database connection
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

        # Create a session
        with Session() as session:
            # Create the State object and add it to the database
            new_state = State(name='Louisiana')
            session.add(new_state)
            session.commit()

            # Retrieve and print the state ID
            state_add = session.query(State).filter(State.name == 'Louisiana').one()
            print("State 'Louisiana' added with ID:", state_add.id)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:4]
    add_louisiana_state(username, password, database_name)
