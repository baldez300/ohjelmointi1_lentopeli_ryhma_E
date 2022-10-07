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

def endcheck():
    sql = f"SELECT co2_consumed FROM game WHERE screen_name = 'gdf' and tickets_amount = '10' and continents_amount ='6'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

print(endcheck())