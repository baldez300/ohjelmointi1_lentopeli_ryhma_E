# at the start of the game saves username and starting location
sql = f"INSERT INTO game (screen_name)" \
      "VALUES({username})" \
    "INSERT INTO game (location)" \
    "VALUES " # player's starting location

# every time player moves to another airport
sql = "INSERT INTO game (location)" \
    "VALUES" #player's current location

# at the end
# laskee nykyisen käyttäjän pisteet ja näyttää ne
# co2.game & location.game

# top 5
# laskutoimitus pisteet kaikille käyttäjille
# näyttää 5 korkeinta pistemäärää
sql = "ORDER BY points_amount DESC"
