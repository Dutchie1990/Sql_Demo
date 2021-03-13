import os
import datetime
import pymysql

username = os.getenv('user')

connection = pymysql.connect(
    host="localhost", user=username, password="", db='Chinook')

try:
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-12-02 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s)", row)
        connection.commit()
finally:
    connection.close()
