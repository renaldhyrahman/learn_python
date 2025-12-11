from app.model import Model
from app.view import View


class Controller:
    def __init__(self):
        self.model = Model(
            commands={
                "start": self.on_start,
                "reset": self.on_reset,
            }
        )
        self.view = View(
            window=self.model.window,
            data_image=(
                self.model.image_tk,
                self.model.image_size,
            ),
            canvas=self.model.canvas,
            labels=self.model.labels,
            buttons=self.model.buttons,
        )

    def run(self):
        self.model.window.mainloop()

    def on_start(self):
        print("start")

    def on_reset(self):
        print("reset")
