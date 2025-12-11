import tkinter as tk

import app.constants as cons
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.boot()

    def boot(self):
        self.setup_root()
        self.load_assets()
        self.setup_canvas()

        self.build_layout()

    def setup_root(self):
        self.root = tk.Tk()
        self.root.title(cons.TITLE)

    def load_assets(self):
        image = Image.open(cons.PATH_IMG)
        self.asset_img = ImageTk.PhotoImage(image)

    def setup_canvas(self):
        self.canvas = tk.Canvas(
            self.root,
            width=cons.SIZE_CANVAS,
            height=cons.SIZE_CANVAS,
            highlightthickness=0,
        )

        img_xcor = cons.SIZE_CANVAS / 2
        img_ycor = cons.SIZE_CANVAS / 2
        self.canvas.create_image(img_xcor, img_ycor, image=self.asset_img)

    def build_layout(self):
        self.canvas.pack(
            padx=cons.SIZE_PADDING_CANVAS,
            pady=cons.SIZE_PADDING_CANVAS,
        )

    def run(self):
        self.root.mainloop()
