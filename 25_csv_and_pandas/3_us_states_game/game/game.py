import turtle as t

import game.config as gc
import pandas as pd  # type: ignore


class Game:
    def __init__(self):
        self.df = pd.read_csv(gc.PATH_CSV)
        self.states = self.df.state.to_list()
        self.is_on = True
        self.user_correct_guess = []
        self.setup_screen()
        self.setup_writer()

    def setup_screen(self):
        self.screen = t.Screen()
        self.screen.setup(width=gc.SCREEN_WIDTH, height=gc.SCREEN_HEIGHT)
        self.screen.bgpic(gc.PATH_IMG)
        self.screen.title(gc.GAME_TITLE)

    def setup_writer(self):
        self.writer = t.Turtle(visible=False)
        self.writer.penup()
        self.writer.speed(0)

    def write_state(
        self, state: str, color: str = "black", is_saved: bool = False
    ):
        data = self.df[self.df.state == state].iloc[0]
        coor = (data.x, data.y)
        self.writer.goto(coor)
        self.writer.color(color)
        self.writer.write(
            data.state, align=gc.STATES_ALIGN, font=gc.STATES_FONT
        )
        if is_saved:
            loc_index = len(self.df_unguessed)
            self.df_unguessed.loc[loc_index] = [data.state, data.x, data.y]

    def write_info(self, info: str):
        self.writer.color("red")
        self.writer.goto(gc.INFO_COOR)
        self.writer.write(info, align=gc.INFO_ALIGN, font=gc.INFO_FONT)

    def game_over(self, is_player_win: bool = False):
        info = "You Win!" if is_player_win else "Game Over"
        self.write_info(info)
        if not is_player_win:
            self.write_missed_states()
            self.df_unguessed.to_csv(gc.PATH_OUTPUT, index=False)
        self.is_on = False
        self.screen.exitonclick()

    def write_missed_states(self):
        dict_unguessed = {
            "states": [],
            "x": [],
            "y": [],
        }
        self.df_unguessed = pd.DataFrame(dict_unguessed)
        for state in self.states:
            if state not in self.user_correct_guess:
                self.write_state(state=state, color="red", is_saved=True)

    def logic_check_input(self, user_input: str):
        if user_input in gc.EXIT_COMMANDS:
            self.game_over()
            return
        if user_input in self.user_correct_guess:
            return
        if user_input not in self.states:
            return
        self.user_correct_guess.append(user_input)
        self.write_state(user_input)

    def play(self):
        score = len(self.user_correct_guess)
        if score == len(self.states):
            self.game_over(is_player_win=True)
            return
        title = f"{score}/50 States Correct"
        prompt = "What's another state name?"
        user_input = self.screen.textinput(title=title, prompt=prompt)
        if user_input is None:
            self.game_over()
            return
        self.logic_check_input(user_input.strip().title())
