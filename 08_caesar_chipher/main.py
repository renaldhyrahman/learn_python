from art import logo as ascii_logo

# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(data_list):
    restart_input, run_or_restart, dictionary = data_list
    if run_or_restart == "restart":
        user_input_restart = None
        while user_input_restart not in [True, False]:
            user_input_restart = (
                input(
                    "\nType 'yes' if you want to go again, "
                    "otherwise type 'no'\n"
                )
                .strip()
                .lower()
            )
            if user_input_restart in ["yes", "y"]:
                restart_input = True
                run_or_restart = "run"
                user_input_restart = True
            elif user_input_restart in ["no", "n"]:
                restart_input = False
                user_input_restart = False
            else:
                user_input_restart = None
        return [restart_input, run_or_restart, dictionary]

    direction = (
        input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
        .strip()
        .lower()
    )
    while direction not in ["encode", "decode"]:
        direction = (
            input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            .strip()
            .lower()
        )

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n").strip())

    result = ""
    for letter in text:
        if letter not in dictionary:
            result += letter
        else:
            if direction == "encode":
                shift_amount = shift
            if direction == "decode":
                shift_amount = shift * -1
            result += dictionary[
                (dictionary.index(letter) + shift_amount) % len(dictionary)
            ]

    print(f"\nHere is the {direction}d result: {result}\n")
    run_or_restart = "restart"
    return [restart_input, run_or_restart, dictionary]


def run_caesar(dictionary):
    print(ascii_logo)
    data = [True, "run", dictionary]
    while data[0]:
        data = caesar(data)


run_caesar(alphabet)
