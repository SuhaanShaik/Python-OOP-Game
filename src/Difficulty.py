class Difficulty:
  def __init__(self, name, rounds, winning_numbers, score_value, xp_value, max_number):
    self.name = name
    self.rounds = rounds
    self.winning_numbers = winning_numbers
    self.xp_value = xp_value
    self.score_value = score_value
    self.max_number = max_number


SUPER_EASY = Difficulty(
        name = "Super Easy",
        rounds = 10,
        winning_numbers = [5, 7, 9, 4, 2],
        score_value = 1,
        xp_value = 5,
        max_number = 10

)

EASY = Difficulty(
        name = "Easy",
        rounds = 5,
        winning_numbers = [5, 7, 9],
        score_value = 3,
        xp_value = 15,
        max_number = 15
)

MEDIUM = Difficulty(
        name = "Medium",
        rounds = 3,
        winning_numbers = [5, 7, 9],
        score_value = 10,
        xp_value = 40,
        max_number = 25
)

HARD = Difficulty(
        name = "Hard",
        rounds = 1,
        winning_numbers = [5, 7],
        score_value = 25,
        xp_value = 75,
        max_number = 50
 )

SUPER_HARD = Difficulty(
        name = "Super Hard",
        rounds = 1,
        winning_numbers = [5],
        score_value = 75,
        xp_value = 150,
        max_number = 100
)

INSANE = Difficulty(
        name = "INSANE",
        rounds = 1,
        winning_numbers = [5],
        score_value = 500,
        xp_value = 500,
        max_number = 1000
)
