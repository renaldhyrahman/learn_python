from dataclasses import dataclass

from model import Model
from view import View

# #######################################


@dataclass
class States:
    is_playing = None
    task = None


# #######################################


class Controller:
    def __init__(self):
        self.states = States()
        self.model = Model()
        self.view = View()

    def input_prompt(self, task):
        """task: 'start'/'compare'/None,
        return: bool"""
        question, accept, reject = [None, None, None]
        match task:
            case "start":
                question = "\nPlay the game?\nType 'y' for yes or 'n' for no: "
                accept = ["y", "yes"]
                reject = ["n", "no"]
            case "compare":
                question = "\nWho has more followers?\nType 'A' or 'B': "
                accept = ["a"]
                reject = ["b"]
            case _:
                question = "\nPress any key to continue\n"
        return self.view.display_input([question, accept, reject])

    def start(self):
        """void"""
        self.states.task = "display: welcome screen"
        self.view.display_ui("welcome")
        self.states.task = "input: play the game?"
        self.states.is_playing = self.input_prompt("start")

    def exit(self):
        """void"""
        self.states.task = "display: exit screen"
        self.view.display_ui("exit")

    def game(self):
        """void"""
        self.states.task = "logic: generate questions"
        questions = self.model.create_question()
        self.states.task = "display: comparison"
        self.view.display_ui("compare", questions)
        self.states.task = "input: A/B"
        self.states.task = "logic: check answer"
        if self.model.check_answer(self.input_prompt("compare")):
            self.states.task = "display: win"
            self.view.display_ui("win", [self.model.player.score])
            if self.model.player.score >= self.model.MAX_SCORE:
                self.states.task = "logic: forced win scenario"
                self.model.reset()
            self.input_prompt(None)
            return
        self.states.task = "display: lose"
        self.view.display_ui("lose", [self.model.player.score])
        self.states.task = "input: continue/start again"
        if self.input_prompt("start"):
            self.model.reset()
            return
        self.states.task = "display: exit"
        self.states.is_playing = False
