import turtle as t


class UiInput:
    def __init__(self):
        self.accepts = ["y", "yes"]
        self.rejects = ["n", "no"]

    def is_restart(self):
        input_user = None
        while input_user not in self.accepts + self.rejects:
            input_user = t.textinput(
                "Game Over", "\nDo you want to restart? Type 'y' or 'n':"
            )
            if input_user is None:
                input_user = "n"
            else:
                input_user = input_user.strip().lower()
        if input_user in self.accepts:
            return True
        else:
            return False
