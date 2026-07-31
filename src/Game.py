import random

from Difficulty import SUPER_EASY
from Achievement import IMPOSSIBLE

class Game:
    def __init__(self, difficulty, player, leaderboard, save_manager):
        self.difficulty = difficulty
        self.player = player
        self.leaderboard = leaderboard
        self.save_manager = save_manager

    def play_game(self):
        print(f"\nDifficulty: {self.difficulty.name}")
        print(f"Welcome {self.player.name}!")

        while True:
            for _ in range(self.difficulty.rounds):
                self.play_round()

            if (
              self.difficulty == SUPER_EASY
              and self.player.current_game_score == self.difficulty.rounds * self.difficulty.score_value
            ):
              self.player.unlock_achievement(IMPOSSIBLE)

            self.player.add_game()
            self.player.update_best_score()
            self.player.current_game_score = 0
            self.leaderboard.update_player(self.player)
            self.save_manager.save(self.leaderboard.players)


            print(
              f"\nGame complete! "
              f"Total Score: {self.player.total_score} | "
              f"Total Wins: {self.player.total_wins}"
            )

            if not self.ask_play_again():
                print("\nThanks for playing!")
                break

    def play_round(self):
        self.player.add_round()
        number = self.generate_random_number()

        if number in self.difficulty.winning_numbers:
            self.player.add_win(self.difficulty.score_value)
            self.player.add_xp(self.difficulty.xp_value)
            self.player.add_difficulty_win(self.difficulty)

            print(
                f"{self.player.name}, you got {number}. "
                f"WINNER!!! +{self.difficulty.score_value} points!"
            )
            print(
                f"+{self.difficulty.xp_value} XP earned "
                f"({self.player.xp}/{self.player.xp_needed_for_next_level})"
            )

        else:
            self.player.add_loss()

            print(
                f"Better luck next time, {self.player.name}. "
                f"You got {number}."
                )

    def generate_random_number(self):
        return random.randint(1, self.difficulty.max_number)

    def ask_play_again(self):
        while True:
            again = input("\nPlay another game? (yes/no): ").strip().lower()

            if again == "yes":
                return True

            elif again == "no":
                return False

            else:
                print("Please enter yes or no.")
