# uusi rivi game tauluun jossa tickets_amount (kuinka monessa maassa käyttäjä on käynyt)
# ALTER TABLE game
# ADD tickets_amount int(20);
# uusi rivi game tauluun jossa continents_amount (kuinka monessa maanosassa käyttäjä on käynyt)
# ALTER TABLE game
# ADD continents_amounts int(20);


# at the start of the game saves username and starting location
sql = f"INSERT INTO game (screen_name)" \
      "VALUES({username})"
sql = "INSERT INTO game (location)" \
    "VALUES " # player's starting location

# every time player moves to another airport
sql = "INSERT INTO game (location)" \ # NO INSERT, UPDATE
    "VALUES" #player's current location
# update tickets_amount
# update continents_amount

# at the end
# laskee nykyisen käyttäjän pisteet ja näyttää ne -> PISTEMÄÄRÄ EI TALLENNU
# co2.game & tickets_amount.game & continents_amount.game

# top 5
# laskutoimitus pisteet kaikille käyttäjille pythonissa
# co2.game & tickets_amount.game & continents_amount.game
# näyttää 5 korkeinta pistemäärää