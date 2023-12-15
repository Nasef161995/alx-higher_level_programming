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
    quary = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ID ASC"
    cursor.execute(quary)

    table = cursor.fetchall()
    for element in table:
        print(element)
    cursor.close()
    db_connection.close()
