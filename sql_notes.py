# TODO: starting values for tickets_amount and continents_amount are 0
# TODO: autoincrement id.game
# TODO: add co2 additions (only at the end?)

import mysql.connector

def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Qi$$%^7Zp7Yj!4rq%ba2hTo!',
        autocommit=True
         )

connection = connect_database()
# --------------------------
# TODO: check if works
# at the start of the game saves username
sql = f"INSERT INTO game (screen_name) VALUES({username})"

# saves starting location
sql = f"INSERT INTO game (location) VALUES({start_airport})"
# --------------------------
# TODO: check if works AND dont include starting or ending airport!!!
# every time player moves to another airport
sql = f"UPDATE game SET location = ({airportIcaoCode}) " \
    "SET tickets_amount = + 1"
# jos pelaaja liikkuu toiseen maanosaan
sql = "UPDATE game SET continents_amount + 1"

# ---------------------------
# DONE AND CHECKED THIS WORKS
def endcheck():
    sql = f"SELECT co2_consumed FROM game WHERE screen_name = ({username}) and tickets_amount = '10' and continents_amount ='7'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

print(endcheck())
# ---------------------------

# top 5
# hakee tietokannasta käyttäjät jotka ovat keränneet 10 lippua ja käyneet 7 maanosassa
# https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursordict.html
# TODO: complete def score()
def score():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT screen_name, co2_consumed FROM game WHERE tickets_amount = '10' and continents_amount ='7'")


# printtaa top 5 listan
# TODO: order by desc, limit print to top 5
print("TOP 5:")
for row in cursor:
    print("* {Name}".format(Name=row['Name']