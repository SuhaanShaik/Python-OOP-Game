class Leaderboard:
    def __init__(self, players = None):
      if players:
        self.players = players
      else:
        self.players = {}


    def find_player(self, player_id):
      return self.players.get(player_id)

    def find_players_by_name(self, name):
      matches = []

      for player in self.players.values():
        if player.name.lower() == name.lower():
          matches.append(player)

      return matches

    def update_player(self, player):
        self.players[player.id] = player

    def display_scores(self):
        print("\nLeaderboard:")

        ranked = sorted(
            self.players.values(),
            key=lambda player: (player.total_score, player.total_wins, player.highest_streak),
            reverse=True
        )

        if not ranked:
            print("No Players yet.")
            return

        for rank, player in enumerate(ranked, start=1):
            print(
                f"#{rank} | "
                f"ID: {player.id} | "
                f"{player.name} | "
                f"Lvl {player.level} | "
                f"Achievements: {len(player.achievements)} | "
                f"XP [{player.xp_bar()}] "
                f"XP: {player.xp}/{player.xp_needed_for_next_level} | "
                f"Score: {player.total_score} points | "
                f"Wins: {player.total_wins} wins | "
                f"{player.win_rate:.1f}% win rate | "
                f"{player.highest_streak} streak "

             )
