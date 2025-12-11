import tkinter as tk

import app.constants as cons
from PIL import ImageTk


class View:
    def __init__(
        self,
        window: tk.Tk,
        canvas: tk.Canvas,
        data_image: tuple[ImageTk.PhotoImage, tuple[float, float]],
    ):
        self.window = window
        self.canvas = canvas
        self.data_image = data_image

        # setups
        self.setup_window()
        self.setup_canvas()

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

    def build_layout(self):
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
