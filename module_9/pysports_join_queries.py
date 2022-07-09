import mysql.connector

config = {
    "user": "root",
    "password": "January-123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

print("-- DISPLAYING PLAYER RECORDS --")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]),
        "\nFirst Name: {}".format(player[1]),
        "\nLast Name: {}".format(player[2]),
        "\nTeam Name: {}\n".format(player[3]))
