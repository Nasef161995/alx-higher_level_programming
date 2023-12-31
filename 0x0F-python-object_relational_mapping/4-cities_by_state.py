#!/usr/bin/python3
"""mysqldb module"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = db_connection.cursor()
    quary = """ SELECT
                    cities.id,
                    cities.name,
                    states.name
                    FROM
                    cities
                    JOIN
                    states
                    ON
                    cities.state_id = states.id
                    ORDER BY id ASC"""
    cursor.execute(quary)
    table = cursor.fetchall()
    for element in table:
        print(element)
    cursor.close()
    db_connection.close()
