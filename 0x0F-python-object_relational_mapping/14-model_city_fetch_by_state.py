#!/usr/bin/python3
"""class city"""

import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    result_cities = session.query(
        State.name,
        City.id,
        City.name).order_by(
        City.id). filter(
            State.id == City.state_id).order_by(
                City.id)

    for element in result_cities:
        print("{}: ({}) {}".format(element[0], element[1], element[2]))

    session.close()
