# import constants as cons

from app.model import Model
from app.view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(
            window=self.model.window,
            canvas=self.model.canvas,
            data_image=(
                self.model.image_tk,
                self.model.image_size,
            ),
        )

    def run(self):
        self.model.window.mainloop()
