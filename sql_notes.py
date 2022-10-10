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
# ---------------------------------------------------------------------------
# saves username - checked and works
sql = f"INSERT INTO game (screen_name) VALUES ('{username}')"

# saves starting location - checked and works
sql = f"UPDATE game SET location = ('{start_airport}') WHERE screen_name = '{username}'"
# ---------------------------------------------------------------------------
# every time player moves to another airport - checked and works
sql = f"UPDATE game SET location = '{airportIcaoCode}' " \
    "SET tickets_amount = tickets_amount + 1"
# if player moves to another continent - checked and works
sql = "UPDATE game SET continents_amount = continents_amount + 1"

# -----------------------------------------------------------------------------
# checks if user has visited 10 countries and 6 continents - checked and works
def check_tickets_continents():
    sql = f"SELECT co2_consumed FROM game WHERE screen_name = '{username}' and tickets_amount = '10' and continents_amount ='6'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

print(check_tickets_continents())
# ---------------------------------------------------------------------------

# top 5, gets 5 users with lowest co2 used and orders by ascending - checked and works
def t5():
    cursor = connection.cursor()
    cursor.execute("SELECT screen_name, co2_consumed FROM game WHERE tickets_amount = '10' and continents_amount ='6' ORDER BY co2_consumed ASC LIMIT 5")
    result = cursor.fetchall()
    return result

print(t5())