import json
import os

from Player import Player

class SaveManager:

  def __init__(self, filename):
    self.filename = filename

  def save(self, players):
    player_data = {}

    for player_id, player in players.items():
      player_data[player_id] = player.to_dict()

    with open(self.filename, "w") as file:
      json.dump(player_data, file, indent=4)

  def load_players(self):
    if not os.path.exists(self.filename):
      return {}

    with open(self.filename, "r") as file:
      data = json.load(file)

    players = {}

    for player_id, player_data in data.items():

      player = Player.from_dict(player_id, player_data)

      players[int(player_id)] = player

    if players:
      Player.next_id = max(players.keys()) + 1

    return players
################################################################################
def choose_difficulty():
  while True:
    print("\n=== Choose your Difficulty===")
    print("1. Super Easy")
    print("2. Easy")
    print("3. Medium")
    print("4. Hard")
    print("5. Super Hard")
    print("6. INSANE")

    choice = input("Select Difficulty: ").strip()

    if choice == "1":
      return SUPER_EASY

    elif choice == "2":
      return EASY

    elif choice == "3":
      return MEDIUM

    elif choice == "4":
      return HARD

    elif choice == "5":
      return SUPER_HARD

    elif choice == "6":
      return INSANE

    else:
      print("Please enter 1, 2, 3, 4, 5, or 6!")
