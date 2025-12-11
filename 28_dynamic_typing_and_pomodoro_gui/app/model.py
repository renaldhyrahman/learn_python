import tkinter as tk
from typing import Callable

import app.constants as cons
from PIL import Image, ImageTk


class Model:
    def __init__(
        self,
        commands: dict[str, Callable[[], None]],
    ):
        self.window = tk.Tk()
        self.commands = commands
        self.create_image()
        self.create_canvas()
        self.create_labels()
        self.create_buttons()

    def create_image(self):
        image = Image.open(cons.PATH_IMG)
        self.image_size = image.size
        self.image_tk = ImageTk.PhotoImage(image)

    def create_canvas(self):
        img_width, img_height = self.image_size
        self.canvas = tk.Canvas(
            self.window,
            width=img_width,
            height=img_height,
            highlightthickness=0,
        )

    def create_labels(self):
        self.labels = {
            "task": tk.Label(),
            "loop": tk.Label(),
        }

    def create_buttons(self):
        self.buttons = {
            "start": tk.Button(
                highlightthickness=0,
                command=self.commands["start"],
            ),
            "reset": tk.Button(
                highlightthickness=0,
                command=self.commands["reset"],
            ),
        }
