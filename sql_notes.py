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
# saves username - checked and works
sql = f"INSERT INTO game (screen_name) VALUES ('{username}')"

# saves starting location - checked and works
sql = f"UPDATE game SET location = ('{start_airport}') WHERE screen_name = '{username}'"
# --------------------------
# TODO: check if works AND dont include starting or ending airport!!!
# every time player moves to another airport - checked and works
sql = f"UPDATE game SET location = '{airportIcaoCode}' " \
    "SET tickets_amount = tickets_amount + 1"
# if player moves to another continent - checked and works
sql = "UPDATE game SET continents_amount = continents_amount + 1"

# ---------------------------
# checks if user has visited 10 countries and 6 continents - checked and works
def check_tickets_continents():
    sql = f"SELECT co2_consumed FROM game WHERE screen_name = '{username}' and tickets_amount = '10' and continents_amount ='6'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

print(check_tickets_continents())
# ---------------------------

# top 5
# hakee tietokannasta käyttäjät jotka ovat keränneet 10 lippua ja käyneet 6 maanosassa
# https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursordict.html
# https://www.tutorialspoint.com/how-to-sort-a-dictionary-in-python
# https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
# TODO: test if works; maybe sort with sql code and fetchmany(5) instead of fetchall?
def score():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT screen_name, co2_consumed FROM game WHERE tickets_amount = '10' and continents_amount ='6'")
    result = cursor.fetchall()
    return result

# TODO: order by desc, limit print to top 5, idk if this shit works yet
# creates another dictionary that sorts by value
score2 = dict(sorted(score.items(), key=lambda x:x[1]))
# prints top5
print("TOP 5:")
for s in range(5):
    print("* {name}".format(Name=row['Name']