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


# lentokentän haku
def search_airport(icao):
     sql = f"SELECT name FROM airport where ident = '{icao}'"
     cursor = connection.cursor()
     cursor.execute(sql)
     result = cursor.fetchall()
     return result

def airportname(use):
     for i in use:
          text = i[0]
     return text

# kysyy käyttäjänimen
username = input("Anna pelinimesi: ")

# tervetuloa printti
print(f"""Tervetuloa pelaamaan lentopeliä {username}.
Tarkoituksenasi on lentää kaikki maanosat läpi keräten maiden lippuja
mahdollisimman pienellä co2-päästöillä""")

# Itse pelin aloitus
print("""                      """)
print("""Helsinki-Vantaa --> EFHK,
Enontekiö Airport --> EFET,
Kokkola-Pietarsaari Airport --> EFKK""")
airport = input("Miltä lentokentältä haluat aloittaa?")


start_airport = search_airport(airport)

start_airport = airportname(start_airport)

print(airport)
print(start_airport)

