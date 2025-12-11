import tkinter as tk

import app.constants as cons
from PIL import Image, ImageTk


class Model:
    def __init__(self):
        self.window = tk.Tk()
        self.create_image()
        self.create_canvas()

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
