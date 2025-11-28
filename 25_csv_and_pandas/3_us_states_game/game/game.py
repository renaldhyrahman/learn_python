import turtle as t

import game.config as gc
import pandas as pd  # type: ignore


class Game:
    def __init__(self):
        self.df = pd.read_csv(gc.PATH_CSV)
        self.states = self.df.state.to_list()
        self.is_on = True
        self.score = 0
        self.user_past_guess = []
        self.setup_screen()

    def setup_screen(self):
        self.screen = t.Screen()
        self.screen.setup(width=gc.SCREEN_WIDTH, height=gc.SCREEN_HEIGHT)
        self.screen.bgpic(gc.PATH_IMG)
        self.screen.title(gc.GAME_TITLE)

    def write_state(self, user_guess: str):
        state = t.Turtle(visible=False)
        state.penup()
        data = self.df[self.df.state == user_guess].iloc[0]
        state.goto(data.x, data.y)
        state.write(data.state, align="center", font=("Courier", 12, "normal"))

    def write_info(self, info: str):
        writer = t.Turtle(visible=False)
        writer.penup()
        writer.color("red")
        writer.write(info, align="center", font=("Courier", 36, "bold"))

    def game_over(self, is_player_win: bool = False):
        info = "You Win!" if is_player_win else "Game Over"
        self.write_info(info)
        self.is_on = False
        self.screen.exitonclick()

    def logic_check_answer(self, user_guess: str):
        if (user_guess not in self.states) or (
            user_guess in self.user_past_guess
        ):
            return
        self.user_past_guess.append(user_guess)
        self.write_state(user_guess)
        self.score += 1

    def play(self):
        if self.score == len(self.states):
            self.game_over(is_player_win=True)
            return
        title = f"{self.score}/50 States Correct"
        prompt = "What's another state name?"
        user_guess = self.screen.textinput(title=title, prompt=prompt)
        if user_guess is None:
            self.game_over()
            return
        self.logic_check_answer(user_guess.strip().title())
