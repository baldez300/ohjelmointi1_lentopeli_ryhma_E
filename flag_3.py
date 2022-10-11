# Count visited countries flags

from collections import Counter
import mysql.connector
import flag


def get_countries_code(code_input):
    sql = f"SELECT iso_country FROM country WHERE country.name = '{code_input}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()  # type of result: list

    flag_list = {}
    for code in result:
        codestr = ''.join(code)
        lippu = flag.flag(codestr)
        print(lippu)
        flag_list[code] = lippu
    return flag_list


def connect_database():
    return mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
        user='.....',
        password='....',
        autocommit=True
    )


connection = connect_database()

flag_input = input("Anna country full name: ")
get_countries_code(flag_input)
