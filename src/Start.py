from Game import Game
from Player import Player
from Leaderboard import Leaderboard
from Save_manager import SaveManager

from Difficulty import (
    SUPER_EASY,
    EASY,
    MEDIUM,
    HARD,
    SUPER_HARD,
    INSANE
)

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

def start():
    save_manager = SaveManager("players.json")

    players = save_manager.load_players()

    leaderboard = Leaderboard(players)

    while True:
        print("\n=== Player Login ===")

        while True:
            returning = input(
                "Are you a returning player? (yes/no): "
            ).strip().lower()

            if returning in ("yes", "no"):
                break

            print("Please enter yes or no.")

        if returning == "yes":

            while True:
                try:
                    player_id = int(input("Enter your player ID: "))

                except ValueError:
                    print("Please enter a valid ID.")
                    continue

                player = leaderboard.find_player(player_id)

                if player:
                    print(f"Welcome back, {player.name}!")
                    break

                print("No player found with that ID.")

        else:

            while True:
                name = input("Enter your name: ").strip()

                if name:
                    break

                print("Name cannot be blank.")

            matches = leaderboard.find_players_by_name(name)

            if matches:
                print("\nPlayers already using that name:")

                for existing in matches:
                    print(
                        f"ID: {existing.id} | "
                        f"{existing.total_score} points | "
                         f"{existing.total_wins} wins"
                    )

                while True:
                    choice = input(
                        "\nCreate a new player anyway? (yes/no): "
                    ).strip().lower()

                    if choice == "yes":
                        player = Player(name)
                        break

                    elif choice == "no":

                        while True:
                            try:
                                player_id = int(
                                    input(
                                        "Enter the player ID you want to use: "
                                    )
                                )

                            except ValueError:
                                print("Please enter a valid ID.")
                                continue

                            player = leaderboard.find_player(player_id)

                            if player and player.name.lower() == name.lower():
                                break

                            print(
                                "That ID does not belong to a player with that name."
                            )

                        break

                    else:
                        print("Please enter yes or no.")

            else:
                player = Player(name)

            if player.id not in leaderboard.players:
                leaderboard.update_player(player)
                save_manager.save(leaderboard.players)

            print(f"\nWelcome {player.name}!")
            if player.games_played == 0:
                print(f"Your player ID is {player.id}.")
                print("Keep this ID if you want your stats to continue.")

        difficulty = choose_difficulty()

        game = Game(
            difficulty = difficulty,
            player=player,
            leaderboard=leaderboard,
            save_manager = save_manager
        )

        game.play_game()

        while True:
          print("\n===== Post Game Menu =====")
          print("1. View Statistics")
          print("2. View Leaderboard")
          print("3. Continue")

          choice = input("Choose an option: ").strip()

          if choice == "1":
            player.display_statistics()

          elif choice == "2":
            leaderboard.display_scores()

          elif choice == "3":
            break

          else:
            print("Invalid choice.")

        while True:
            another_player = input(
                "\nWould another player like to play? (yes/no): "
            ).strip().lower()

            if another_player == "yes":
                break

            elif another_player == "no":
                print("\nFinal leaderboard:")
                leaderboard.display_scores()
                print("Thanks for playing!")
                save_manager.save(leaderboard.players)
                return

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


start()
