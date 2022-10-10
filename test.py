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

def score():
    cursor = connection.cursor()
    cursor.execute("SELECT screen_name, co2_consumed FROM game WHERE tickets_amount = '10' and continents_amount ='6' ORDER BY co2_consumed ASC LIMIT 5;")
    result = cursor.fetchall()
    return result


print(score())

# creates another dictionary that sorts by value
#score2 = dict(sorted(score.items(), key=lambda x:x[1]))
# prints top5
#print("TOP 5:")
#for s in range(5):
#    print("* {name}".format(Name=row['Name']


# -----------------------------------------------------------------