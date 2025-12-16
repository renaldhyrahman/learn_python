import tkinter as tk

import app.constants as cons
from PIL import Image, ImageTk


class View:
    def __init__(self):
        self.boot()

    def boot(self):
        self.setup_window()
        self.load_assets()
        self.setup_states()
        self.setup_canvas()
        self.setup_labels()
        self.setup_buttons()
        self.build_layout()

        # attach observer
        self.state_score.trace_add("write", self.obs_score)
        self.state_question.trace_add("write", self.obs_question)

        # normalize state/trigger observer
        self.state_score.set(0)
        self.state_question.set("Placeholder")

    def setup_window(self):
        self.window = tk.Tk()
        self.window.title(cons.ConfigView.TITLE.value)
        self.window.configure(
            bg=cons.ConfigView.THEME_COLOR.value,
            padx=cons.Size.PADDING.value,
            pady=cons.Size.PADDING.value,
        )

    def setup_states(self):
        self.state_score = tk.IntVar()
        self.state_question = tk.StringVar()

    def load_assets(self):
        img_true = Image.open(cons.Path.IMG_TRUE.value)
        img_false = Image.open(cons.Path.IMG_False.value)
        self.img_true = ImageTk.PhotoImage(img_true)
        self.img_false = ImageTk.PhotoImage(img_false)

    def setup_canvas(self):
        width, heigth = cons.Size.CANVAS.value
        self.canvas = tk.Canvas(
            self.window,
            width=width,
            height=heigth,
        )
        text_xcor = width / 2
        text_ycor = heigth / 2
        self.canvas_text = self.canvas.create_text(
            (text_xcor, text_ycor),
            font=cons.ConfigView.FONT.value,
        )

    def setup_labels(self):
        self.label_scoreboard = tk.Label(
            self.window,
            bg=cons.ConfigView.THEME_COLOR.value,
            fg=cons.ConfigView.FG_COLOR_SCORE.value,
        )

    def setup_buttons(self):
        self.button_true = tk.Button(
            self.window,
            image=self.img_true,
            border=0,
            highlightthickness=0,
            command=lambda: print("True"),
        )
        self.button_false = tk.Button(
            self.window,
            image=self.img_false,
            border=0,
            highlightthickness=0,
            command=lambda: print("False"),
        )

    def build_layout(self):
        padding = cons.Size.PADDING.value
        self.label_scoreboard.grid(column=1, row=0, pady=padding)
        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=padding,
        )
        self.button_true.grid(column=0, row=2, pady=padding)
        self.button_false.grid(column=1, row=2, pady=padding)

    def obs_score(self, *args):
        score = self.state_score.get()
        self.label_scoreboard.config(text=f"Score: {score}")

    def obs_question(self, *args):
        question = self.state_question.get()
        self.canvas.itemconfig(self.canvas_text, text=question)

    def run(self):
        self.window.mainloop()
