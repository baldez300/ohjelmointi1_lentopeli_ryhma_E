
import geopy.distance
import mysql.connector

def connect_database():
    return mysql.connector.connect(
         host="127.0.0.1",
         port=3306,
         database="flight_game",
         user="root",
         password="TiVi2022!",
         autocommit=True
         )


connection = connect_database()

def airport_location(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        lat = i[0]
        lon = i[1]
    location = (lat, lon)
    return location


print("""                      """)
print("""Helsinki-Vantaa --> EFHK,
Enontekiö Airport --> EFET,
Kokkola-Pietarsaari Airport --> EFKK""")
airport = input("Miltä lentokentältä haluat aloittaa?")

current_airport_location = airport_location(airport)


next_airport_location = airport_location(input("Minne haluat mennä: "))

distance = geopy.distance.distance(current_airport_location, next_airport_location).km.__round__(2)
print(f"Matkan pituus: {distance} km")


# Co2 määrä kilogrammoina
co2perkm = 0.225

co2used = distance * co2perkm

print(f"co2 päästöt: {co2used.__round__(2)} kg")
