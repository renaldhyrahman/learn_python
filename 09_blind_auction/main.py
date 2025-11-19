from os import name as os_name
from os import system as os_system

from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


def display_clear():
    if os_name == "nt":
        _ = os_system("cls")
    else:
        _ = os_system("clear")


def auction():
    print(logo)
    continue_bidding = True
    bids = {}
    while continue_bidding:
        name = input("What is your name?: ")
        price = float(input("What is your bid?: $ "))
        bids[name] = price
        should_continue = input(
            "Are there any other bidders? Type 'yes or 'no'.\n"
        ).lower()
        if should_continue in ["yes", "y"]:
            display_clear()
        else:
            continue_bidding = False
            display_clear()
    print(
        f"The Winner is {max(bids, key=bids.get)} with a bid of "
        f"${max(bids.values())}"
    )


auction()
