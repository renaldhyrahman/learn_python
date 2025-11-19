import random
from json.encoder import INFINITY

from display import display

# ######################################

debug_ace_revealed = {
    "index_rank": 12,
    "suit": "club",
    "rank": "A",
    "value": 0,
    "hidden": False,
}
debug_ace_hidden = {
    "index_rank": 12,
    "suit": "diamond",
    "rank": "A",
    "value": 0,
    "hidden": True,
}
debug_king_revealed = {
    "index_rank": 11,
    "suit": "heart",
    "rank": "K",
    "value": 10,
    "hidden": False,
}
debug_king_hidden = {
    "index_rank": 11,
    "suit": "spade",
    "rank": "K",
    "value": 10,
    "hidden": True,
}
debug_queen_revealed = {
    "index_rank": 10,
    "suit": "club",
    "rank": "Q",
    "value": 10,
    "hidden": False,
}
debug_queen_hidden = {
    "index_rank": 10,
    "suit": "diamond",
    "rank": "Q",
    "value": 10,
    "hidden": True,
}
debug_jack_revealed = {
    "index_rank": 9,
    "suit": "heart",
    "rank": "J",
    "value": 10,
    "hidden": False,
}
debug_jack_hidden = {
    "index_rank": 9,
    "suit": "spade",
    "rank": "J",
    "value": 10,
    "hidden": True,
}

debug_numbered_1_revealed = {
    "index_rank": 2,
    "suit": "heart",
    "rank": "4",
    "value": 4,
    "hidden": False,
}
debug_numbered_1_hidden = {
    "index_rank": 0,
    "suit": "diamond",
    "rank": "2",
    "value": 2,
    "hidden": True,
}
debug_numbered_2_revealed = {
    "index_rank": 4,
    "suit": "diamond",
    "rank": "6",
    "value": 6,
    "hidden": False,
}
debug_numbered_3_revealed = {
    "index_rank": 3,
    "suit": "diamond",
    "rank": "5",
    "value": 5,
    "hidden": False,
}


# ######################################


def game_setting():
    return {
        "init_chips": 1000,
        "deck_amount": 1,
        "cut_card": 0.75,
        "delay": 1,
        "min_bet": 100,
        "blackjack_payout": 1.5,
    }


# ######################################


class Game:
    def __init__(self, settings):
        self.settings = settings.copy()
        self.states = None
        self.deck = []
        self.cut_card = INFINITY
        self.deck_stage = None
        self.dealer = None
        self.player = None

    def init_game(self):
        self.states = {
            "playing": False,
            "shuffle": True,
            "round_in_progress": False,
            "announcement": None,
        }
        self.dealer = {
            "cards": [],
            "totals": 0,
        }
        self.player = {
            "min_bet": self.settings["min_bet"],
            "chips": self.settings["init_chips"],
            "current_hand": {
                "cards": [],
                "totals": 0,
                "bet": None,
                "name": "hand_1",
            },
            "insurance": None,
            "hands": [],
        }

    @staticmethod
    def update_totals(user):
        user["totals"] = 0
        for card in user["cards"]:
            if not card["hidden"]:
                if card["value"] != 0:
                    user["totals"] += card["value"]
                elif user["totals"] < 11:
                    user["totals"] += 11
                else:
                    user["totals"] += 1

    def refresh_ui(self, user=None):
        if user:
            self.update_totals(user)
        display("ui", self)

    def announcement(self, announcement=None):
        self.states["announcement"] = announcement
        self.refresh_ui()

    def update_deck_level(self):
        frame = 5
        deck_current = len(self.deck)
        deck_max = 52 * self.settings["deck_amount"]
        deck_cut = self.cut_card

        # Avoid division by zero (edge case if cut_card == deck_max)
        if (deck_max - deck_cut) <= 0:
            self.deck_stage = 0
            return

        proportion = (deck_max - deck_current) / (deck_max - deck_cut)
        level = int(proportion * frame)

        # Clamp
        self.deck_stage = min(max(level, 0), frame - 1)

    def deck_create(self):
        card_suits = ["spade", "heart", "club", "diamond"]
        card_ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]
        card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 0]
        deck = [
            {
                "index_rank": index_rank,
                "suit": suit,
                "rank": rank,
                "value": card_value[index_rank],
                "hidden": True,
            }
            for _, suit in enumerate(card_suits)
            for index_rank, rank in enumerate(card_ranks)
        ]
        self.deck = deck * self.settings["deck_amount"]
        self.cut_card = int(len(self.deck) * self.settings["cut_card"])

    def hand_create(self):
        # player_cards = self.player["current_hand"]["cards"]
        hand_new = {
            "name": f"hand_{len(self.player["hands"]) + 2}",
            "bet": self.player["bet"],
            "totals": None,
            "cards": [self.player["cards"].pop()],
        }
        self.update_totals(hand_new)
        self.player["hands"] += [hand_new]

    def card_draw(self, user, hidden):
        card = self.deck.pop()
        if not hidden:
            card["hidden"] = False
        user["cards"] += [card]
        self.update_deck_level()
        self.refresh_ui(user)

    def card_reveal(self):
        dealer = self.dealer
        card = dealer["cards"][-1]
        card["hidden"] = False
        self.refresh_ui(dealer)

    def check_insurance(self):
        card_value_dealer = self.dealer["cards"][0]["value"]
        chips = self.player["chips"]
        bet = self.player["bet"]

        if card_value_dealer == 0 and chips >= (bet / 2):
            return True
        return False

    def check_dealer_blackjack(self):
        dealer = self.dealer
        hidden_card = dealer["cards"][-1]
        if hidden_card:
            _totals = dealer["totals"]
            hidden_card["hidden"] = False
            self.update_totals(dealer)
            if dealer["totals"] == 21 and len(dealer["cards"]) == 2:
                hand_blackjack = True
            else:
                hand_blackjack = False
            hidden_card["hidden"] = True
            dealer["totals"] = _totals
            return hand_blackjack
        else:
            self.update_totals(dealer)
            if dealer["totals"] == 21 and len(dealer["cards"]) == 2:
                return True
            return False

    def check_player_blackjack(self):
        player = self.player
        if player["totals"] == 21 and len(player["cards"]) == 2:
            return True
        return False

    def check_any_blackjack(self):
        player_blackjack = self.check_player_blackjack()
        dealer_blackjack = self.check_dealer_blackjack()
        if player_blackjack and dealer_blackjack:
            return "tie"
        if dealer_blackjack:
            return "dealer"
        if player_blackjack:
            return "player"
        return None

    def check_split(self):
        player = self.player
        card_1 = player["cards"][0]
        card_2 = player["cards"][1]
        player_have_enough_chip = player["chips"] >= player["bet"]
        if card_1["rank"] == card_2["rank"] and player_have_enough_chip:
            return True
        return False

    def check_double(self):
        player = self.player
        if player["chips"] >= player["bet"] and len(player["cards"]) == 2:
            return True
        return False

    def action_insurance(self):
        bet = self.player["bet"]
        bet_insurance = int(bet / 2)
        self.player["chips"] -= bet_insurance
        self.player["insurance"] = bet_insurance

    def action_split(self):
        bet = self.player["bet"]
        hands = self.player["hands"]
        self.player["chips"] -= bet
        self.hand_create()
        self.refresh_ui()
        # self.card_draw(self.player, False)
        # Debug: Forced another split
        if len(hands) < 4:
            self.player["cards"] += [debug_ace_revealed]
            self.update_totals(self.player)
            self.refresh_ui()
        else:
            self.card_draw(self.player, False)

    def action_double(self):
        self.player["bet"] *= 2

    def payout(self, amount):
        self.player["chips"] += amount

    def payout_settlement(self, any_blackjack, responds_insurance):
        blackjack_payout = self.settings["blackjack_payout"]
        player = self.player
        dealer = self.dealer
        bet = player["bet"]
        self.card_reveal()

        # Return bet to player if tie
        if any_blackjack == "tie":
            self.payout(bet)
        # Settle Insurance
        if any_blackjack in ["tie", "dealer"] and responds_insurance:
            self.payout(bet)
        # Settle Blackjack
        if any_blackjack == "player":
            self.payout(bet + (round(blackjack_payout * bet)))
        # Settle
        if not any_blackjack:
            self.update_totals(dealer)
            self.update_totals(player)
            if player["totals"] <= 21 and player["totals"] >= dealer["totals"]:
                self.payout(bet * 2)

        # Reveal and reset
        player["insurance"] = None
        player["bet"] = None
        # self.states["round_in_progress"] = False
        self.refresh_ui()

    def start_round(self):
        self.states["announcement"] = None
        player = self.player
        responds_insurance = False
        # responds_split = False
        self.update_deck_level()

        if self.states["shuffle"]:
            random.shuffle(self.deck)
            # self.announcement("Dealer Shuffling Cards")
            # display("shuffle", self)
            # self.announcement("Dealer Placing Cut Cards")
            # display("cut_cards", self)
            self.states["shuffle"] = False
        # self.announcement("Waiting for your bet...")
        # bet = input_user("bets", self.player)
        # Debug: Force bet = 100
        bet = 100
        self.refresh_ui()
        player["chips"] -= bet
        player["bet"] = bet
        self.announcement("Dealing cards...")
        # self.card_draw(self.dealer, False)
        # self.card_draw(player, False)
        # self.card_draw(self.dealer, True)
        # self.card_draw(player, False)

        # Debug Forced card
        self.dealer["cards"] += [debug_ace_revealed]
        # self.refresh_ui(self.dealer)
        self.player["cards"] += [debug_ace_revealed]
        # self.refresh_ui(self.player)
        self.dealer["cards"] += [debug_ace_hidden]
        # self.refresh_ui(self.dealer)
        self.player["cards"] += [debug_ace_revealed]
        # self.refresh_ui(self.player)
        self.update_totals(self.dealer)
        self.update_totals(self.player)

        self.announcement()

        # Check if insurance and early blackjack
        any_blackjack = self.check_any_blackjack()
        insurance = self.check_insurance()
        if insurance:
            self.announcement("Waiting for your responds...")
            # responds_insurance = input_user("insurance")
            # Debug: Forced reject insurance
            responds_insurance = False
            if responds_insurance:
                self.announcement("Insurance accepted...")
                self.action_insurance()
            self.announcement("Dealer checking his card...")
            # Check if dealer blackjack
            if any_blackjack == "dealer":
                self.announcement("Dealer Blackjack !")
            else:
                self.player["insurance"] = 0
                self.announcement("Dealer does not blackjack !")
        # Check if player blackjack
        if any_blackjack:
            self.announcement("Settling payout...")
            self.payout_settlement(any_blackjack, responds_insurance)
            return None

        self.announcement()

        # Check if split
        split = self.check_split()
        while split:
            # responds_split = input_user("split")
            # Debug: Forced accept split
            responds_split = True
            if responds_split:
                self.action_split()
            else:
                break
            split = self.check_split()

        # Complete every hands
        hands = [
            {
                "bet": bet,
                "cards": player["cards"],
            }
        ] + player["hands"]
        # _hands = []
        for hand in hands:
            player["bet"] = hand["bet"]
            player["cards"] = hand["cards"]
            # Check if double
            double = self.check_double()
            if double:
                responds_double = input_user("double", player)
                if responds_double:
                    self.action_double()

            hit = True
            while hit:
                if self.check_player_blackjack():
                    break
                if player["totals"] <= 21:
                    responds_hit = input_user("hit", player)
                    if responds_hit:
                        self.card_draw(player, False)
                    else:
                        hit = False
                else:
                    hit = False

        # Dealer's logic
        self.card_reveal()

        # Settle every hands
        any_blackjack = self.check_any_blackjack()
        self.payout_settlement(any_blackjack, responds_insurance)

        # Round end clean up -> update states

        input("Debug start_round")

        return "Debug: Warning"


# ######################################


def input_validation(question, input_accept, input_reject=None):
    result = False

    if input_accept is list:
        user_input = input(question).strip().lower()
        while user_input not in (input_accept + input_reject):
            user_input = input(question).strip().lower()
        if user_input in input_accept:
            result = True

    if type(input_accept) in [int, float]:
        flag = True
        while flag:
            try:
                user_input = input(question)
                result = int(user_input)
                if result < input_reject or result > input_accept:
                    flag = True
                else:
                    flag = False
            except ValueError:
                flag = True

    return result


def input_user(task, player=None):
    question = None
    input_accept = []
    input_reject = []

    match task:
        case "start":
            question = """
        Play Blackjack?
        Type 'y' for start playing, 'n' for exit:
        """
            input_accept = ["y", "yes"]
            input_reject = ["n", "no", "e", "exit", "q", "quit"]
        case "bets":
            question = rf"""
        How many chips you want to Bet?
        Type your amount (min: {player["min_bet"]}, max: {player["chips"]}):
        """
            input_accept = player["chips"]
            input_reject = player["min_bet"]
        case "insurance":
            question = r"""
        Do you want Insurance?
        Type 'y' for yes, 'n' for no:
        """
            input_accept = ["y", "yes", "i", "insurance"]
            input_reject = ["n", "no"]
        case "split":
            question = r"""
        Do you want to Split?
        Type 'y' for yes, 'n' for no:
        """
            input_accept = ["y", "yes", "s", "split"]
            input_reject = ["n", "no"]
        case "double":
            question = rf"""
        Current bet: {player["bet"]}
        Do you want to Double?
        Type 'y' for yes/double, 'n' for no:
            """
            input_accept = ["y", "yes", "d", "double"]
            input_reject = ["n", "no"]
        case "hit":
            question = rf"""
        Current bet: {player["bet"]}
        Hit or Stand?
        Type 'y' for yes/hit, 'n' for stand:
            """
            input_accept = ["y", "yes", "h", "hit"]
            input_reject = ["n", "no", "s", "stand"]

    result = input_validation(question, input_accept, input_reject)
    return result


# ######################################


def blackjack():
    display("start")
    game = Game(game_setting())
    game.init_game()

    # Input: Start
    # game.states["playing"] = input_user("start")
    # Debug: Auto-Start
    game.states["playing"] = True

    if not game.states["playing"]:
        return display("exit")

    while game.states["playing"]:
        game.deck_create()
        game.states["round_in_progress"] = True
        while game.states["round_in_progress"]:
            winner = game.start_round()
            print(f"Winner: {winner}")
            # Debug Forced end round
            game.states["round_in_progress"] = False
        print(f"deck: {len(game.deck)}")
        print(f"cut_card: {game.cut_card}")

        # Debug: forced exit
        game.states["playing"] = False

    display("ui", game)
    return None


# ######################################

blackjack()
