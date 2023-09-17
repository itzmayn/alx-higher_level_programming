#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” in the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:4]

    # Create the database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Create the State "California" and the City "San Francisco"
        california = State(name="California")
        san_francisco = City(name="San Francisco", state=california)
        session.add(california)
        session.add(san_francisco)
        session.commit()
