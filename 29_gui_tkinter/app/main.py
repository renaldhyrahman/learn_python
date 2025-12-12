import tkinter as tk

import app.constants as cons
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.boot()

    def boot(self):
        self.setup_root()
        self.load_assets()
        self.setup_widgets()

        self.build_layout()

    def setup_root(self):
        self.root = tk.Tk()
        self.root.title(cons.TITLE)
        self.root.config(
            padx=cons.Size.PADDING.value,
            pady=cons.Size.PADDING.value,
        )

    def setup_widgets(self):
        self.setup_canvas()
        self.setup_label()
        self.setup_entry()
        self.setup_buttons()

    def load_assets(self):
        image = Image.open(cons.PATH_IMG)
        self.asset_img = ImageTk.PhotoImage(image)

    def setup_canvas(self):
        size_canvas = cons.Size.CANVAS.value
        self.canvas = tk.Canvas(
            self.root,
            width=size_canvas,
            height=size_canvas,
            highlightthickness=0,
        )

        img_xcor = size_canvas / 2
        img_ycor = size_canvas / 2
        self.canvas.create_image(img_xcor, img_ycor, image=self.asset_img)

    def setup_label(self):
        self.label_website = tk.Label(
            self.root,
            text="Website:",
            font=cons.FONT_TEXT,
        )
        self.label_username = tk.Label(
            self.root,
            text="Email/Username:",
            font=cons.FONT_TEXT,
        )
        self.label_password = tk.Label(
            self.root,
            text="Password:",
            font=cons.FONT_TEXT,
        )

    def setup_entry(self):
        self.entry_webstite = tk.Entry(
            self.root,
            width=35,
            font=cons.FONT_TEXT,
        )
        self.entry_username = tk.Entry(
            self.root,
            width=35,
            font=cons.FONT_TEXT,
        )
        self.entry_password = tk.Entry(
            self.root,
            width=21,
            font=cons.FONT_TEXT,
        )

    def setup_buttons(self):
        self.button_generate = tk.Button(
            self.root,
            text="Generate Password",
            font=cons.FONT_TEXT,
            highlightthickness=0,
        )
        self.button_add = tk.Button(
            self.root,
            text="Add",
            width=36,
            font=cons.FONT_TEXT,
            highlightthickness=0,
        )

    def build_layout(self):
        self.canvas.grid(column=0, row=0, columnspan=3)

        self.label_website.grid(column=0, row=1)
        self.entry_webstite.grid(
            column=1,
            row=1,
            columnspan=2,
            sticky=tk.W,
        )

        self.label_username.grid(
            column=0,
            row=2,
        )
        self.entry_username.grid(
            column=1,
            row=2,
            columnspan=2,
            sticky=tk.W,
        )

        self.label_password.grid(
            column=0,
            row=3,
        )
        self.entry_password.grid(
            column=1,
            row=3,
            sticky=tk.W,
        )
        self.button_generate.grid(
            column=2,
            row=3,
            sticky=tk.W,
        )

        self.button_add.grid(
            column=1,
            row=4,
            columnspan=2,
            sticky=tk.W,
        )

    def run(self):
        self.root.mainloop()
