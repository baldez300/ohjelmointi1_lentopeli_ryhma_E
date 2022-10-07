import mysql.connector
import geopy.distance

def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='TiVi2022!',
        autocommit=True
         )


connection = connect_database()


# lentokenttien haku

def select_country(country):
    sql = f"select airport.name, ident from airport  inner join country on airport.iso_country = country.iso_country  where country.name='{country}' and type in ('medium_airport', 'large_airport') order by rand() limit 5;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(f"{i[0]}: {i[1]}")

    if result == [ ]:
        print("Anna lentokenttä")
    else:
        return result


# def select_country_list(tuple):
#     countrylist = []
#     for i in tuple:
#         countrylist.append(i)
#     return countrylist


# maan lentokentän valinta
def select_country_airport(airport, iso):
    sql = f"select name from airport where ident='{airport}' and iso_country = '{iso}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print("\n------------------------")
        print(f"Olet nyt lentokentällä: {i[0]}")

    if result == []:
        print("Anna kelvollinen lentokentän icao-koodi")
    else:
        return result


# maiden haku
def search_country_in_continent(continent):
    sql = f"SELECT name FROM country where continent = '{continent}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    countrylist = []
    for i in result:
        print(i[0])
        countrylist.append(i[0])
    if result == [ ]:
        print("Anna kelvollinen maanosa")
    else:
        return countrylist

# Maan iso_countryn hakeminen

def isocountry(country):
    sql = f"SELECT iso_country FROM country WHERE name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        isocode = i[0]

    return isocode

# Lentokentän nimen hakeminen ainoastaan
def search_airport(icao):
    sql = f"SELECT name FROM airport where ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        text = i[0]

    return text


# Lentokenttien gps sijainnit
def airport_location(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        lat = i[0]
        lon = i[1]
    location = (lat, lon)
    return location

# co2 päästöt kilogrammoina per kilometri
co2perkm = 0.225
# co2 kokonaispäästöt
co2overallused = 0

username = input("Anna pelinimesi: ")

print(f"""\nTervetuloa pelaamaan lentopeliä {username}.
Tarkoituksenasi on lentää kaikki maanosat läpi keräten maiden lippuja
mahdollisimman pienellä co2-päästöillä""")


# Itse pelin aloitus
print("""                      """)
print("------------------------")
print("""Helsinki-Vantaa --> EFHK
Enontekiö Airport --> EFET
Kokkola-Pietarsaari Airport --> EFKK""")
print("------------------------")
print("""                      """)

starticaos = ("EFHK", "EFET", "EFKK")

while True:
    airport = input("Miltä lentokentältä haluat aloittaa?: ").upper()
    if airport in starticaos:
        break
    else:
        print("Anna joku yllämainituista icao-koodeista!")
start_airport = search_airport(airport)

count = "EU"
print("""                      """)
print("------------------------")
print(f"Olet lentokentällä: {start_airport}")
print("------------------------\n")
# Loop through above functions to travel more.
program_running = True

while program_running:
    # input user command
    # userinput = input("Anna 'lopeta', 'hae_maanosaan', vai 'hae_maan': ")
    print("Jos haluat lentää saman maanosan sisällä syötä: Toiseen maahan\nJos haluat vaihtaa maanosaa syötä: Toiseen maanosaan\n ")
    #TODO lisää alku printtiin kaikki mahdolliset vaihtoehdot
    userinput = input("Minne haluat lentää: ").lower()
    print("\n------------------------")
    if userinput == "lopeta":
        print("Moikka ja tervetuloa uudelleen..!")
        program_running = False

    #TODO Muuta lopeta tilalle ns. pelin oma lopetus eikä lopeta komentoa
    elif userinput == "päästöt":
        print(f"Kokonais co2 päästöstösi ovat {co2overallused} km")
        print("------------------------\n")
    # elif userinput == "sijainti":
    #     print(f"{search_airport(airport)}")
    elif userinput == "toiseen maanosaan":
        continentloop = []
        nameloop = []
        icaoloop = []
        while not continentloop:
            count = input("Valitse maanosan nimi AF(Africa), AS(Asia), EU(Europe), \nNA(North-America), OC(Oceania), SA(South-America): ")
            print("------------------------")
            continentloop = search_country_in_continent(count)
            print("------------------------")
        while not nameloop:
            countryNm = input("Anna sen maan nimi, johon haluat matkustaa: ")
            if countryNm in continentloop:
                print("\n------------------------")
                nameloop = select_country(countryNm)
                print("------------------------\n")
        while not icaoloop:
            airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä kirjoittamalla ICAO-koodi: ")
            iso_country = isocountry(countryNm)
            icaoloop = select_country_airport(airportIcaoCode, iso_country)
        current_airport_location = airport_location(airport)
        next_airport_location = airport_location(airportIcaoCode)
        distance = geopy.distance.distance(current_airport_location, next_airport_location).km.__round__(2)
        co2used = (distance * co2perkm).__round__(2)
        co2overallused += co2used
        print(f"\nMatka lentokentälle oli {distance} km")
        print(f"Co2 päästöjä syntyi {co2used} kg")
        print("------------------------")
        airport = airportIcaoCode

    elif userinput == "toiseen maahan":
        countryloop = []
        icaoloop = []
        search_country_in_continent(count)
        print("------------------------\n")

        while not countryloop:
            countryNm = input("Anna sen maan nimi, johon haluat matkustaa: ")
            print("------------------------")
            countryloop = select_country(countryNm)
            print("------------------------")
        while not icaoloop:
            iso_country = isocountry(countryNm)
            airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä kirjoittamalla ICAO-koodi: ")
            icaoloop = select_country_airport(airportIcaoCode, iso_country)
            print("------------------------")
        current_airport_location = airport_location(airport)
        next_airport_location = airport_location(airportIcaoCode)
        distance = geopy.distance.distance(current_airport_location, next_airport_location).km.__round__(2)
        airport = airportIcaoCode
        co2used = (distance * co2perkm).__round__(2)
        co2overallused += co2used
        print(f"\nMatka lentokentälle oli {distance} km")
        print(f"Co2 päästöjä syntyi {co2used} kg")
        print("------------------------")
        airport = airportIcaoCode
