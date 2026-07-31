from Achievement import *
from Difficulty import (
    SUPER_EASY,
    EASY,
    MEDIUM,
    HARD,
    SUPER_HARD,
    INSANE
)

class Player:
    next_id = 1
    def __init__(self, name):
        self.name = name
        self.id = Player.next_id
        Player.next_id += 1
        self.total_wins = 0
        self.total_score = 0
        self.games_played = 0
        self.total_rounds = 0
        self.total_losses = 0
        self.best_score = 0
        self.current_streak = 0
        self.highest_streak = 0
        self.current_game_score = 0
        self.super_easy_wins = 0
        self.easy_wins = 0
        self.medium_wins = 0
        self.hard_wins = 0
        self.super_hard_wins = 0
        self.insane_wins = 0
        self.xp = 0
        self.level = 1
        self.achievements = set()

    def add_win(self, amount):
      self.total_wins += 1
      self.total_score += amount
      self.current_game_score += amount
      self.current_streak += 1

      if self.current_streak >= self.highest_streak:
        self.highest_streak = self.current_streak

      self.check_achievements()

    def add_loss(self):
      self.total_losses += 1
      self.current_streak = 0

      self.check_achievements()

    def add_difficulty_win(self, difficulty):
      if difficulty == SUPER_EASY:
        self.super_easy_wins += 1

      elif difficulty == EASY:
        self.easy_wins += 1

      elif difficulty == MEDIUM:
        self.medium_wins += 1

      elif difficulty == HARD:
        self.hard_wins += 1

      elif difficulty == SUPER_HARD:
        self.super_hard_wins += 1

      elif difficulty == INSANE:
        self.insane_wins += 1


      self.check_achievements()


    def add_round(self):
      self.total_rounds += 1

      self.check_achievements()

    def add_game(self):
      self.games_played += 1


    def unlock_achievement(self, achievement):
      if achievement.name not in self.achievements:
          self.achievements.add(achievement.name)

          print("ACHIEVEMENT UNLOCKED!")
          print(f"{achievement.name}")
          print(achievement.description)

    def check_achievements(self):

      # Total Wins
      if self.total_wins >= 1:
        self.unlock_achievement(FIRST_WIN)

      if self.total_wins >= 10:
        self.unlock_achievement(ROOKIE)

      if self.total_wins >= 100:
        self.unlock_achievement(EXPERIENCED)

      if self.total_wins >= 500:
        self.unlock_achievement(VETERAN)

      if self.total_wins >= 1000:
        self.unlock_achievement(LEGENDARY)

      # Levels
      if self.level >= 5:
        self.unlock_achievement(APPRENTICE)

      if self.level >= 20:
        self.unlock_achievement(WIZARD_OF_LUCK)

      if self.level >= 50:
        self.unlock_achievement(FORTUITOUS_WARLOCK)

      if self.level >= 100:
        self.unlock_achievement(THE_CHAMPION)

      # Lifetime Score
      if self.total_score >= 1000:
        self.unlock_achievement(DEDICATED)

      if self.total_score >= 10000:
        self.unlock_achievement(THE_BIGGEST_FISH)

      # Difficulty Wins
      if self.hard_wins >= 20:
        self.unlock_achievement(COURAGEOUS)

      if self.super_hard_wins >= 15:
        self.unlock_achievement(SUPREME)

      if self.insane_wins >= 1:
        self.unlock_achievement(INSANITY)

      if self.insane_wins >= 10:
        self.unlock_achievement(WTF)

      # Win on every difficulty
      if (
        self.super_easy_wins > 0
        and self.easy_wins > 0
        and self.medium_wins > 0
        and self.hard_wins > 0
        and self.super_hard_wins > 0
        and self.insane_wins > 0
      ):
        self.unlock_achievement(MASTER)

      if self.highest_streak >= 5:
        self.unlock_achievement(ON_FIRE)

      if self.highest_streak >= 10:
        self.unlock_achievement(UNSTOPPABLE)

      # Loss Achievements
      if self.total_losses >= 1:
        self.unlock_achievement(BAD_LUCK)

      if self.total_losses >= 10:
        self.unlock_achievement(ROUGH_START)

      if self.total_losses >= 100:
        self.unlock_achievement(UNLUCKY)

      if self.total_losses >= 500:
        self.unlock_achievement(CURSED)

      if self.total_losses >= 1000:
        self.unlock_achievement(THE_BLACK_HOLE)

      # Low Win Rate Achievement
      if self.total_rounds >= 100 and self.win_rate < 10:
        self.unlock_achievement(WHY_ARE_YOU_HERE)


      # Comeback Achievement
      if self.total_losses >= 50 and self.current_streak >= 10:
        self.unlock_achievement(THE_COMEBACK)


    def update_best_score(self):
      if self.current_game_score > self.best_score:
        self.best_score = self.current_game_score

    @property
    def xp_needed_for_next_level(self):
      return int(500 * (1.25 ** (self.level - 1)))

    def add_xp(self, amount):
      self.xp += amount

      while self.xp >= self.xp_needed_for_next_level:
        self.xp -= self.xp_needed_for_next_level
        self.level += 1

        print(f"\n yLEVEL UP! You reached Level {self.level}!")

      self.check_achievements()

    def xp_bar(self, length=10):
      progress = self.xp / self.xp_needed_for_next_level

      filled = int(progress * length)

      return "█" * filled + "░" * (length - filled)

    @property
    def win_rate(self):
      if self.total_rounds == 0:
        return 0

      return (self.total_wins / self.total_rounds) * 100


    def display_statistics(self):

      print("\n========== PLAYER STATISTICS ==========")
      print(f"Name: {self.name}")
      print(f"ID: {self.id}")

      print("\n---------- Progress ----------")
      print(f"Level : {self.level}")
      print(
          f"XP    : [{self.xp_bar()}] "
          f"{self.xp}/{self.xp_needed_for_next_level}"
      )

      print(f"Next Level: {self.xp_needed_for_next_level - self.xp} XP needed")

      print("\n---------- Overall ----------")

      print(f"Total Score : {self.total_score}")
      print(f"Total Wins  : {self.total_wins}")
      print(f"Total Losses : {self.total_losses}")
      print(f"Games Played : {self.games_played}")
      print(f"Rounds Played : {self.total_rounds}")
      print(f"Win Rate    : {self.win_rate:.1f}%")

      print("\n---------- Records ----------")

      print(f"Best Game Score : {self.best_score}")
      print(f"Highest Streak  : {self.highest_streak}")

      print("\n---------- Difficulty Wins ----------")

      print(f"Super Easy : {self.super_easy_wins}")
      print(f"Easy       : {self.easy_wins}")
      print(f"Medium     : {self.medium_wins}")
      print(f"Hard       : {self.hard_wins}")
      print(f"Super Hard : {self.super_hard_wins}")
      print(f"INSANE     : {self.insane_wins}")

      print("\n---------- Achievements ----------")

      if not self.achievements:
        print("No achievements unlocked yet.")

      else:
        print(f"Achievements Unlocked: {len(self.achievements)}")

        for achievement in sorted(self.achievements):
          print(f" 🏆 {achievement}")

      input("\nPress Enter to return to the menu...")

    def to_dict(self):
      return {
          "name": self.name,
          "id": self.id,
          "total_score": self.total_score,
          "total_wins": self.total_wins,
          "games_played": self.games_played,
          "total_rounds": self.total_rounds,
          "best_score": self.best_score,
          "total_losses": self.total_losses,
          "highest_streak": self.highest_streak,
          "current_streak": self.current_streak,
          "super_easy_wins": self.super_easy_wins,
          "easy_wins": self.easy_wins,
          "medium_wins": self.medium_wins,
          "hard_wins": self.hard_wins,
          "super_hard_wins": self.super_hard_wins,
          "insane_wins": self.insane_wins,
          "level": self.level,
          "xp": self.xp,
          "achievements": list(self.achievements)
      }

    @classmethod
    def from_dict(cls, player_id, data):
      player = cls(data["name"])

      player.id = data["id"]
      player.total_score = data["total_score"]
      player.total_wins = data["total_wins"]
      player.games_played = data["games_played"]
      player.total_rounds = data.get("total_rounds", 0)
      player.best_score = data.get("best_score", 0)
      player.total_losses = data.get("total_losses", 0)
      player.highest_streak = data.get("highest_streak", 0)
      player.current_streak = data.get("current_streak", 0)
      player.super_easy_wins = data.get("super_easy_wins", 0)
      player.easy_wins = data.get("easy_wins", 0)
      player.medium_wins = data.get("medium_wins", 0)
      player.hard_wins = data.get("hard_wins", 0)
      player.super_hard_wins = data.get("super_hard_wins", 0)
      player.insane_wins = data.get("insane_wins", 0)
      player.level = data.get("level", 1)
      player.xp = data.get("xp", 0)
      player.achievements = set(data.get("achievements", []))

      return player
