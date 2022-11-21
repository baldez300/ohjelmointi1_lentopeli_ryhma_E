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

# saves username - checked and works
sql = f"INSERT INTO game (screen_name) VALUES ('{username}')"

# saves starting location - checked and works
sql = f"UPDATE game SET location = 'FI' WHERE screen_name = '{username}'"

# every time player moves to another airport - checked and works
sql = f"UPDATE game SET location = ('{isocountry}') WHERE screen_name = '{username}'"
# every time player moves to another country - checked and works
sql = f"UPDATE game SET tickets_amount = tickets_amount + 1 WHERE screen_name = '{username}'"
# if player moves to another continent - checked and works
sql = f"UPDATE game SET continents_amount = continents_amount + 1 WHERE screen_name = '{username}'"

# checks if user has visited 10 countries and 6 continents - checked and works
sql = f"SELECT co2_consumed FROM game WHERE screen_name = '{username}' and tickets_amount = '10' and continents_amount ='6'"

# updates user's co2_used - checked and works
sql = f"UPDATE game SET co2_consumed = ('{co2_overall_used}') WHERE screen_name = '{username}'"

# top 5, gets 5 users with lowest co2 used and orders by ascending - checked and works
sql = "SELECT screen_name, co2_consumed FROM game WHERE tickets_amount = '10' and continents_amount ='6' ORDER BY co2_consumed ASC LIMIT 5"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

# checks if player is in t5 - checked and works
sql = "SELECT screen_name, co2_consumed FROM game WHERE tickets_amount = '10' and continents_amount ='6' ORDER BY co2_consumed ASC LIMIT 5"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
names = []
for name in result:
    names.append(name[0])
print(names)

if username in names:
    print("Olet top 5 -listalla")
else:
    print("Et ole top 5 -listalla")
