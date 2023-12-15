#!/usr/bin/python3
"""mysqldb module"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    db_connection = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY ID ASC")

    table = cursor.fetchall()
    for element in table:
        print(element)

    cursor.close()
    db_connection.close()
