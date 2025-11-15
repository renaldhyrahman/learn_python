from art import logo as ascii_logo
from playing_cards import deck as ascii_deck
from os import name as os_name, system as os_system
import time

def display_clear():
    if os_name == 'nt': _ = os_system('cls')
    else: _ = os_system('clear')
    print(ascii_logo)
    # print("#################################################################################################")

def card_splitlines(cards):
    ascii_cards = []
    for card in cards:
        if card["hidden"]:
            ascii_cards += [ascii_deck["blank"]]
        else:
            suit = card["suit"]
            card_index = card["index_rank"]
            ascii_cards += [ascii_deck[suit][card_index]]
    # splitlines
    return [ascii_card.splitlines() for ascii_card in ascii_cards]

def display_cards(cards, user):
    if user == "dealer":
        # Fetch ascii for cards
        if len(cards) > 0:
            result = card_splitlines(cards)
            # zip
            for lines in zip(*result): print("".join(lines))
        else: print("\n\n\n\n")

def display_hands(player):
    if len(player["hands"]) < 1: return
    for hand in player["hands"]:
        hand_info = rf"""

bet     : {hand["bet"]}
{hand["name"]}  : {hand["totals"]}

"""
        result = card_splitlines(hand["cards"]) + [hand_info.splitlines()]
        for lines in zip(*result): print("".join(lines))

def display_announcement(data_game):
    states = data_game.states
    print(rf"""
        {states["announcement"] if states["announcement"] else " "}""")

def display_shuffle(data_game):
    ascii_shuffle = [r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      ||||||||||||||||||||||||||
      ||||||||||||||||||||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      |||||||||||      |||||||||
      |||||||||||      |||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      |||||||              |||||
      |||||||              |||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      |||                    |||
      |||                    |||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      |||||||              |||||
      |||||||              |||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
            
      |||||||||||      |||||||||
      |||||||||||      |||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      ||||||||||||||||||||||||||
      ||||||||||||||||||||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
      ||||||||||||||||||||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
          ||||||||||||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
          
              ||||||||||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \

                  ||
    """, r"""
               .+++++.
              | ~~~~~ |
              ) '*_*' (
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )
               '.._..'
             _,/\   /\,_
            /    ':'    \
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'          ==
             _,/\   /\,_
            /    ':'    \
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'          ==
             _,/\   /\,_        ==
            /    ':'    \       ==
    """]

    for frame in ascii_shuffle:
        display_clear()
        print(frame)
        display_announcement(data_game)
        time.sleep(data_game.settings["delay"] / 2)

def display_cut_card(data_game):
    ascii_cut_card = [r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'          ==      --Cut Card
             _,/\   /\,_        ==
            /    ':'    \       ==
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'          ==    --  Cut Card
             _,/\   /\,_        ==
            /    ':'    \       ==
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'          ==  __    Cut Card
             _,/\   /\,_        ==
            /    ':'    \       ==
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'          ==__      Cut Card
             _,/\   /\,_        ==
            /    ':'    \       ==
    """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==        Cut Card
             _,/\   /\,_        ==
            /    ':'    \       ==
        """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==
             _,/\   /\,_        ==
            /    ':'    \       ==
        """]

    for frame in ascii_cut_card:
        display_clear()
        print(frame)
        display_announcement(data_game)
        time.sleep(data_game.settings["delay"] / 2)

def display_dealer(data_game):
    ascii_dealer = [r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==
             _,/\   /\,_        ==
            /    ':'    \       ==
        """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==
             _,/\   /\,_        ==
            /    ':'    \       --
        """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==
             _,/\   /\,_        ==
            /    ':'    \
        """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==
             _,/\   /\,_        --
            /    ':'    \
        """, r"""
               .+++++.          ==
              | ~~~~~ |         ==
              ) '*_*' (         ==
              (  ._.  )         ==
               '.._..'        __==
             _,/\   /\,_
            /    ':'    \
        """]

    print(ascii_dealer[data_game.deck_stage])

def display_table(data_game):
    dealer = data_game.dealer
    player = data_game.player

    display_cards(dealer["cards"])
    print(rf"""
      Dealer's hand   : {dealer["totals"]}
    --------------------------
      Total chips     : {player["chips"]}
      Insurance       : {player["insurance"] if player["insurance"] else "-"}""")
    display_cards(player["cards"])
    display_hands(player)

def display_info(data_game):
    player = data_game.player

    print(rf"""
    
    
    
    """)

def display_ui(data_game):
    display_clear()
    display_dealer(data_game)
    display_announcement(data_game)
    display_table(data_game)
    display_info(data_game)
    time.sleep(data_game.settings["delay"])

# ######################################

def display(task, data_game = None):
    match task:
        case "start": display_clear()
        case "shuffle":display_shuffle(data_game)
        case "cut_cards": display_cut_card(data_game)
        case "ui": display_ui(data_game)
        case "exit":
            display_clear()
            print("Thank you for your visit.")
        case _:
            if os_name == 'nt': _ = os_system('cls')
            else: _ = os_system('clear')
