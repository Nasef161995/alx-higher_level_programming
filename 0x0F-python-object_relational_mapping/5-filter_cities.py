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
    quary = """SELECT
                cities.name
                FROM
                cities
                JOIN
                states
                ON
                cities.state_id = states.id
                WHERE
                states.name LIKE '{:s}'
                ORDER BY cities.id ASC""".format(argv[4])
    cursor.execute(quary)
    table = cursor.fetchall()
    if table:
        for row in table[:-1]:
            for i in row:
                print(i, end=", ")
        print(table[-1][0])
    else:
        print()
    cursor.close()
    db_connection.close()
