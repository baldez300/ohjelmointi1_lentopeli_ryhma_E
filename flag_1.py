# Count visited countries flags

from collections import Counter
import mysql.connector
import flag


def connect_database():
    return mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='....',
         password='.....',
         autocommit=True
         )


connection = connect_database()

flag_input = input("Anna iso_country code: ")
sql = f"SELECT iso_country FROM country WHERE iso_country = '{flag_input}';"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchone()  # type of result: list

while not result:
    print("Error input. Try again...")
    flag_input = input("Anna iso_country code: ")
    sql = f"SELECT iso_country FROM country WHERE iso_country = '{flag_input}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()  # type of result: list

flag_list = []
for code in result:
    flag = flag.flag(code)
    flag_list = {code: flag}
print(flag_list)
