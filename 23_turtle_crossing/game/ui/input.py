import turtle as t


class UiInput:
    def __init__(self):
        self.accepts = ["y", "yes"]
        self.rejects = ["n", "no"]

    def is_restart(self, is_win: bool):
        input_user = None
        while input_user not in self.accepts + self.rejects:
            if is_win:
                title = "You Win"
            else:
                title = "Game Over"
            input_user = t.textinput(
                title, "\nDo you want to restart? Type 'y' or 'n':"
            )
            if input_user is None:
                input_user = "n"
            else:
                input_user = input_user.strip().lower()
        if input_user in self.accepts:
            return True
        else:
            return False
