'''
Caleb Rummel
July 9, 2022
CSD 310 - Module 9
Assingment 9.3
'''

import mysql.connector

config = {
    "user": "root",
    "password": "January-123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#INSERT new player
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")

cursor = db.cursor()
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

print("-- DISPLAYING PLAYER RECORDS AFTER INSERT --")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]),
        "\nFirst Name: {}".format(player[1]),
        "\nLast Name: {}".format(player[2]),
        "\nTeam Name: {}\n".format(player[3]))

#UPDATE new player
cursor = db.cursor()
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

cursor = db.cursor()
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")


print("-- DISPLAYING PLAYER RECORDS AFTER UPDATE --")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]),
        "\nFirst Name: {}".format(player[1]),
        "\nLast Name: {}".format(player[2]),
        "\nTeam Name: {}\n".format(player[3]))


#DELETE new player
cursor = db.cursor()
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

cursor = db.cursor()
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

print("-- DISPLAYING PLAYER RECORDS AFTER DELETE --")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]),
        "\nFirst Name: {}".format(player[1]),
        "\nLast Name: {}".format(player[2]),
        "\nTeam Name: {}\n".format(player[3]))
