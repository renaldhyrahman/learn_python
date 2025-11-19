from os import name as os_name
from os import system as os_system

ASCII_LOGO = r"""
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/
"""

ASCII_VS = r"""
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""


class View:
    def __init__(self):
        self.states = None

    @staticmethod
    def display_clear():
        """void"""
        if os_name == "nt":
            os_system("cls")
        else:
            os_system("clear")

    @staticmethod
    def display_input(input_list):
        """input_list: [question, accept, reject],
        return: bool"""
        question, accept, reject = input_list
        input_user = None
        if accept:
            while input_user not in accept + reject:
                input_user = input(question).strip().lower()
                if input_user in accept:
                    return True
        else:
            input(question)
        return False

    def display_ui(self, task, options=None):
        """task: 'welcome'/'exit'/'compare',
        options: [question1, question2]/[score]"""
        self.display_clear()
        print(ASCII_LOGO)
        try:
            match task:
                case "welcome":
                    print("\nWelcome to Higher or Lower\n")
                case "exit":
                    print("\nThank you for playing.")
                case "win":
                    print(f"You are correct! Current score: {options[0]}")
                case "lose":
                    print(f"You Lose! Final score: {options[0]}")
                case "compare":
                    question_1, question_2 = options
                    print(
                        f"\nCompare A: "
                        f"{question_1['name']}, a {question_1['description']}"
                        f", from {question_1['country']}."
                    )
                    print(f"{ASCII_VS}")
                    print(
                        f"Against B:"
                        f" {question_2['name']}, a {question_2['description']}"
                        f", from {question_2['country']}.\n"
                    )
        except TypeError:
            print("Error: display_ui, Unexpected Input")
            print(f"task: {task}")
            print(f"options: {options}")
