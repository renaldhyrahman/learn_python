from os import name as os_name
from os import system as os_system

from art import logo as ascii_art


def display_clear():
    """Reset the console output based on operating system (OS)"""
    if os_name == "nt":
        _ = os_system("cls")
    else:
        _ = os_system("clear")
    print(ascii_art)


def input_user(input_question, validation_check):
    """Validate input from user"""
    flag = True
    data = None

    if validation_check == "number":
        while flag:
            data = input(input_question).strip()
            try:
                data = float(data)
                flag = False
            except ValueError:
                print(f"Invalid Input! '{data}' is not a number.")
        return data

    if validation_check == "operator":
        while flag:
            data = input(input_question).strip()
            if data in ["+", "-", "*", "/"]:
                flag = False
            else:
                print(f"Invalid input! '{data}' is not a operator.")
        return data

    while flag:
        data = input(input_question).lower().strip()
        if data in ["y", "yes", "n", "no", "q", "quit", "e", "exit"]:
            flag = False
    if data in ["y", "yes"]:
        return "y"
    if data in ["n", "no"]:
        return "n"
    return "quit"


def calculator():
    flag = True
    result = None
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    while flag:
        if result is None:
            display_clear()
            input_1 = input_user("\nWhat's the first number?: ", "number")
        else:
            input_1 = result
            print(f"\nCalculate with {result}")
        input_operator = input_user(
            "Pick an operator ( + - * / ): ", "operator"
        )
        input_2 = input_user("What's the next number?: ", "number")
        if input_2 == 0 and input_operator == "/":
            result = input_1
            print("\nError: Division by Zero")
        else:
            result = operations[input_operator](input_1, input_2)
            print(f"\n {input_1} {input_operator} {input_2} = {result}")
        input_4 = input_user(
            f"\nType 'y' to continue calculating with {result},\n"
            f"type 'n' to start a calculation,\n"
            f"type 'quit' to quit program.\n",
            "restart",
        )
        if input_4 == "n":
            result = None
        if input_4 == "quit":
            flag = False
    display_clear()
    print("\nThank you for using calculator.")


calculator()
