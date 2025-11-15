from os import name as os_name, system as os_system
from art import logo as ascii_logo
import random

def display_clear():
    if os_name == "nt": os_system("cls")
    else: os_system("clear")

def input_validation(question, input_accept, input_reject = None):
    if not question: return None
    result = None
    response_user = None
    while response_user not in input_accept + input_reject:
        response_user = input(question)
        if response_user in input_accept: result = True
        if response_user in input_reject: result = False
    return result

def input_user(task):
    question = None
    input_accept = []
    input_reject = []
    match task:
        case "start":
            question = f"\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
            input_accept = ["y", "yes"]
            input_reject = ["n", "no"]
        case "card":
            question = f"\nType 'y' to get another card, type 'n' to pass: "
            input_accept = ["y", "yes"]
            input_reject = ["n", "no"]
        case "continue":
            question = f"\nPlay another round? Type 'y' or 'n': "
            input_accept = ["y", "yes"]
            input_reject = ["n", "no"]

    return input_validation(question, input_accept, input_reject)

class Game:
    def __init__(self):
        self.states = {
            "continue": False,
            "win": 0,
            "lose": 0,
            "tie": 0,
        }
        self.round = 1
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.player = {
            "cards": [],
            "score": 0,
            "bust": False,
        }
        self.comp = {
            "cards": [],
            "score": 0,
            "bust": False,
        }

    @staticmethod
    def check_blackjack(user):
        if len(user["cards"]) == 2 and user["score"] == 21: return True
        return False

    @staticmethod
    def update_score(user):
        result = 0
        for card in user["cards"]:
            if card == 11 and result < 11: result += 11
            elif card == 11: result += 1
            else: result += card
        if result > 21: user["bust"] = True
        user["score"] = result

    def display(self):
        states = self.states
        player = self.player
        comp = self.comp
        display_clear()
        print(ascii_logo)
        print(f"Round: {self.round} | Win: {states['win']} | Lose: {states['lose']} | Tie: {states['tie']}")
        print(f"\nDealer cards : {comp['cards']}, current score: {comp['score']}")
        print(f"Your cards   : {player['cards']}, current score: {player['score']}")

    def get_card(self, user):
        user["cards"] += [random.choice(self.deck)]
        self.update_score(user)

    def restart(self):
        self.player = {
            "cards": [],
            "score": 0,
            "bust": False,
        }
        self.comp = {
            "cards": [],
            "score": 0,
            "bust": False,
        }

    def deal_cards(self):
        self.get_card(self.comp)
        for _ in range(2): self.get_card(self.player)
        self.display()

    def action(self, user):
        self.get_card(user)
        self.display()

    def dealer_logic(self):
        comp = self.comp
        self.action(comp)
        comp_blackjack = self.check_blackjack(comp)
        if comp_blackjack: return
        while comp["score"] < self.player["score"] and comp["score"] < 17:
            self.action(comp)
            if comp["bust"]: break
        self.display()

    def check_winner(self):
        player = self.player
        comp = self.comp
        states = self.states
        player_blackjack = self.check_blackjack(player)
        comp_blackjack = self.check_blackjack(comp)
        self.display()
        if player_blackjack:
            win = 1
            print("\nYou Win! You got BLACKJACK !")
        elif comp_blackjack:
            win = 0
            print("\nYou Lose! Dealer got BLACKJACK !")
        elif player["bust"]:
            win = 0
            print("\nYou Lose! You BUST !")
        elif comp["bust"]:
            win = 1
            print("\nYou Win! Dealer BUST !")
        elif self.player["score"] > self.comp["score"]:
            win = 1
            print("\nYou win !")
        elif self.player["score"] < self.comp["score"]:
            win = 0
            print("\nYou lose !")
        else:
            win = 2
            print("\nGame tie !")
        if win == 2: states["tie"] += 1
        elif win == 1: states["win"] += 1
        else: states["lose"] += 1

    def start(self):
        player = self.player
        comp = self.comp
        self.deal_cards()
        if self.check_blackjack(player): return
        respond_card = input_user("card")
        while respond_card:
            self.action(player)
            if player["bust"]: respond_card = False
            else: respond_card = input_user("card")
        if player["bust"]: return
        self.dealer_logic()
        if comp["bust"]: return
        if self.check_blackjack(comp): return

def blackjack():
    display_clear()
    game = None
    start_game = input_user("start")
    if start_game:
        game = Game()
        game.states["continue"] = True
    while start_game:
        while game.states["continue"]:
            game.start()
            game.check_winner()
            game.states["continue"] = input_user("continue")
            if game.states["continue"]:
                game.round += 1
                game.restart()
            else:
                start_game = False
    print("\nThank you for playing.")

blackjack()
