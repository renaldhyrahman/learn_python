import tkinter as tk

import app.constants as cons
from PIL import ImageTk


class View:
    def __init__(
        self,
        window: tk.Tk,
        data_image: tuple[ImageTk.PhotoImage, tuple[float, float]],
        canvas: tk.Canvas,
        labels: dict[str, tk.Label],
        buttons: dict[str, tk.Button],
    ):
        self.window = window
        self.data_image = data_image
        self.canvas = canvas
        self.labels = labels
        self.buttons = buttons

        # setups
        self.setup_window()
        self.setup_canvas()
        self.setup_labels()
        self.setup_buttons()

        # layout
        self.build_layout()

    def setup_window(self):
        self.window.title(cons.TITLE)
        self.window.geometry(f"{cons.SIZE_SCREEN}x{cons.SIZE_SCREEN}")
        self.window.config(
            bg=cons.Color.YELLOW.value,
        )

    def setup_canvas(self):
        image, (img_width, img_height) = self.data_image
        xcor = img_width / 2
        ycor = img_height / 2

        self.canvas.config(
            bg=cons.Color.YELLOW.value,
        )

        self.canvas.create_image(
            xcor,
            ycor,
            image=image,
        )
        self.canvas.create_text(
            xcor,
            # offset text 25px to the bottom
            ycor + 25,
            text="00:00",
            fill=cons.Color.WHITE.value,
            font=cons.Font.TIMER.value,
        )

    def setup_labels(self):
        self.labels["task"].config(
            bg=cons.Color.YELLOW.value,
            fg=cons.Color.GREEN.value,
            font=cons.Font.TITLE.value,
        )
        self.labels["loop"].config(
            bg=cons.Color.YELLOW.value,
            fg=cons.Color.GREEN.value,
            font=cons.Font.TEXT.value,
        )

    def setup_buttons(self):
        self.buttons["start"].config(
            padx=10,
            bg=cons.Color.WHITE.value,
            font=cons.Font.TEXT.value,
        )
        self.buttons["reset"].config(
            padx=10,
            bg=cons.Color.WHITE.value,
            font=cons.Font.TEXT.value,
        )

    def build_layout(self):
        self.window.columnconfigure((0, 2), weight=1, uniform="a")
        self.window.columnconfigure(1, weight=3)
        self.window.rowconfigure((0, 2), weight=1, uniform="a")
        self.window.rowconfigure(1, weight=3)
        # self.window.grid_propagate(False)

        self.labels["task"].grid(column=1, row=0)
        self.canvas.grid(column=1, row=1)
        self.buttons["start"].grid(column=0, row=2, sticky=tk.NE)
        self.labels["loop"].grid(column=1, row=2, sticky=tk.N)
        self.buttons["reset"].grid(column=2, row=2, sticky=tk.NW)
