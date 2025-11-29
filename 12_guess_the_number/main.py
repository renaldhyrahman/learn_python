import random
from dataclasses import dataclass
from os import name as os_name
from os import system as os_system

# #######################################

ASCII_LOGO = r"""
  ________                              ___________.__              _______               ___.
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/
"""  # noqa (E501)

# #######################################


class Game:
    def __init__(self):
        self.states = States()
        self.past_guess = []

    @staticmethod
    def input_validation(question, options):
        """args = question: string, options: list or any integer
        return = one of the options or None"""
        if type(question) is not str or type(options) not in [list, int]:
            return None
        result = None
        if type(options) is list:
            while result not in options:
                result = input(question).strip().lower()
        else:
            while type(result) is not int:
                result = input(question).strip().lower()
                try:
                    result = int(result)
                except ValueError:
                    result = None
        return result

    def input_user(self, task):
        """args = task: "start", "difficulty", "guess", "continue"
        return = bool/int or None"""
        if task not in ["start", "difficulty", "guess", "continue"]:
            return None
        question = None
        accept = None
        reject = None
        match task:
            case "start":
                question = (
                    "\nPlay Guess The Number?."
                    "\nType 'y' for yes or 'n' for no: "
                )
                accept = ["y", "yes"]
                reject = ["n", "no"]
            case "difficulty":
                question = "\nChoose a difficulty. Type 'easy' or 'hard': "
                accept = ["e", "easy"]
                reject = ["h", "hard"]
            case "guess":
                question = "\nMake a guess: "
                accept = self.states.secret_number
            case "continue":
                question = "\nType 'y' for yes or 'n' for no: "
                accept = ["y", "yes"]
                reject = ["n", "no"]
        if type(accept) is list:
            if self.input_validation(question, accept + reject) in accept:
                return True
            else:
                return False
        return self.input_validation(question, accept)

    def create(self):
        self.states.is_playing = True
        self.states.continue_playing = True

    def reset(self):
        self.states = States()
        self.past_guess = []

    def display(self, task=None):
        """args = task: string
        return = None"""
        if task not in ["welcome", "start", "guess", "win", "lose", "exit"]:
            return None
        states = self.states
        if os_name == "nt":
            os_system("cls")
        else:
            os_system("clear")
        print(ASCII_LOGO)
        match task:
            case "welcome":
                print("\nWelcome to the Number Guessing Game!\n")
            case "start":
                min_number = states.range_number[0]
                max_number = states.range_number[1]
                print(
                    f"\nI'm thinking of a number between {min_number} and {max_number}"  # noqa (E501)
                )
            case "guess":
                info = states.high_or_low
                attempts = (
                    f"{states.lives} attempt{'' if states.lives == 1 else 's'}"
                )
                if info:
                    high_number = []
                    low_number = []
                    for number in self.past_guess:
                        if number > states.secret_number:
                            high_number += [number]
                        else:
                            low_number += [number]
                    if info == "high":
                        print("\n         Too High.")
                    if info == "low":
                        print("\n         Too Low.")
                    hint = ""
                    if len(low_number):
                        hint += f" higher than {max(low_number)}"
                    if len(low_number) and len(high_number):
                        hint += ","
                    if len(high_number):
                        hint += f" lower than {min(high_number)}"
                    print(f"Hint:{hint}")
                print(f"\nYou have {attempts} remaining to guess the number.")
            case "win":
                print("         YOU WIN !")
                print(
                    f"You guessed the correct Number! ({states.secret_number})"
                )
                print("\nPlay another round?")
            case "lose":
                print("         YOU LOSE !")
                print(f"The number was: {states.secret_number}")
                print("\nPlay another round?")
            case "exit":
                print("\nThank you for playing!\n")
        return None

    def create_secret_number(self):
        states = self.states
        states.secret_number = random.choice(
            range(states.range_number[0], states.range_number[1] + 1)
        )

    def set_difficulty(self):
        states = self.states
        if self.input_user("difficulty"):
            states.mode = "easy"
            states.lives = states.difficulty.easy
        else:
            states.mode = "hard"
            states.lives = states.difficulty.hard

    def game_logic(self):
        states = self.states
        self.display("guess")
        user_guess = self.input_user("guess")
        if user_guess == states.secret_number:
            states.player_win = True
            states.is_playing = False
        else:
            states.lives -= 1
            self.past_guess += [user_guess]
            if user_guess > states.secret_number:
                states.high_or_low = "high"
            else:
                states.high_or_low = "low"
        if states.lives < 1:
            states.is_playing = False

    def is_player_win(self):
        if self.states.player_win:
            self.display("win")
        else:
            self.display("lose")

    def start(self):
        states = self.states
        states.player_win = False
        self.create_secret_number()
        self.display("start")
        self.set_difficulty()
        while states.is_playing:
            self.game_logic()
        self.is_player_win()
        if not self.input_user("continue"):
            states.continue_playing = False
        else:
            self.reset()
            self.create()


# #######################################


@dataclass
class Difficulty:
    easy = 10
    hard = 5


@dataclass
class States:
    range_number = [1, 100]
    difficulty = Difficulty()
    secret_number = None
    is_playing = False
    continue_playing = False
    mode = None
    lives = None
    high_or_low = None
    player_win = None


def guess_a_number():
    game = Game()
    game.create()
    game.display("welcome")
    game.states.continue_playing = game.input_user("start")
    while game.states.continue_playing:
        game.start()
    game.display("exit")


# #######################################

guess_a_number()
