import mysql.connector


def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='username',
        password='password',
        autocommit=True
         )
connection = connect_database()


# maanosien haku
def search_country_in_continent(continent):
    sql = f"SELECT name FROM country where continent = '{continent}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(i[0])

    if not result:
        print("Wrong entry, try gain..")
    else:
        return result

# maan haku
def select_country(country):
    sql = f"select airport.name, ident from airport  inner join country on airport.iso_country = country.iso_country  where country.name='{country}' and type in ('medium_airport', 'large_airport') order by rand() limit 5;"
    cursor = connection.curso()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(f"{i[0]}: {i[1]}")

    if not result:
        print("Wrong entry, try gain..")
    else:
        return result


# maan lentokenttähaku
def select_country_airport(airport):
    sql = f"select name from airport where ident='{airport}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(f"WELCOME TO: {i[0]}")
        print("...")

    if not result:
        print("Wrong entry, try gain..")
    else:
        return result


# Loop through above functions to travel more.
program_running = True
count = 'EU'
while program_running:
    # input user command
    userinput = input("Anna 'lopeta', 'hae_maanosaan', vai 'hae_maan': ")
    if userinput == 'lopeta':
        print("Moikka ja tervetuloa uudelleen..!")
        program_running = False

    elif userinput == 'hae_maanosaan':
        count = input("Valitse maanosan nimi AF(Africa), AS(Asia), EU(Europe), "
                      "NA(North-America), OC(Oceania), SA(South-America): ")
        search_country_in_continent(count)
        print("...")

        countryNm = input("Anna sen maan nimi, johon haluat matkustaa: ")
        print("...")
        select_country(countryNm)
        print("...")

        airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä kirjoittamalla ICAO-koodi: ")
        select_country_airport(airportIcaoCode)

    elif userinput == 'hae_maan':
        search_country_in_continent(count)
        print("...")

        countryNm = input("Anna sen maan nimi, johon haluat matkustaa: ")
        print("...")
        select_country(countryNm)
        print("...")

        airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä kirjoittamalla ICAO-koodi: ")
        select_country_airport(airportIcaoCode)
        print("...")
