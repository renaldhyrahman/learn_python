import tkinter as tk
from typing import Callable

import app.constants as cons
from app.state import State
from PIL import ImageTk


class View:
    def __init__(
        self,
        window: tk.Tk,
        state: State,
        data_image: tuple[ImageTk.PhotoImage, tuple[float, float]],
        canvas: tk.Canvas,
        labels: dict[str, tk.Label],
        buttons: dict[str, tk.Button],
        mode_idle: Callable[[], None],
    ):
        self.window = window
        self.state = state
        self.data_image = data_image
        self.canvas = canvas
        self.labels = labels
        self.buttons = buttons
        # attached observer
        self.state.task.trace_add("write", self.obs_task)
        self.state.counter_secs.trace_add("write", self.obs_counter_secs)
        self.state.counter_loop.trace_add("write", self.obs_counter_loop)
        # setups/configs
        self.setup_window()
        self.setup_canvas()
        self.setup_labels()
        self.setup_buttons()
        # layout
        self.build_layout()
        # normalize state
        mode_idle()

    def obs_task(self, *args):
        task = self.state.task.get()
        transition_map = {
            "Idle": cons.Color.BLACK.value,
            "Work": cons.Color.GREEN.value,
            "Short Break": cons.Color.PINK.value,
            "Long Break": cons.Color.RED.value,
        }
        self.labels["task"].config(text=task, fg=transition_map[task])

    def obs_counter_secs(self, *args):
        self.canvas.itemconfig(self.timer_text, text=self.format_time())

    def obs_counter_loop(self, *args):
        cur_loop = self.state.counter_loop.get()
        if cur_loop == 0:
            return self.labels["loop"].config(text="")
        text_loop = " ".join(["✔" for _ in range(cur_loop)])
        self.labels["loop"].config(text=text_loop)

    def format_time(self):
        counter_secs = self.state.counter_secs.get()
        mins, secs = divmod(counter_secs, 60)
        return "{:02d}:{:02d}".format(mins, secs)

    def setup_window(self):
        self.window.title(cons.TITLE)
        self.window.geometry(f"{cons.SIZE_SCREEN}x{cons.SIZE_SCREEN}")
        self.window.config(bg=cons.Color.YELLOW.value)

    def setup_canvas(self):
        image, (img_width, img_height) = self.data_image
        xcor = img_width / 2
        ycor = img_height / 2

        self.canvas.config(bg=cons.Color.YELLOW.value)
        self.canvas.create_image(
            xcor,
            ycor,
            image=image,
        )
        self.timer_text = self.canvas.create_text(
            xcor,
            # offset text 25px to the bottom
            ycor + 25,
            text="xx:xx",
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
        self.window.columnconfigure((0, 2), weight=1)
        self.window.columnconfigure(1, weight=2)
        self.window.rowconfigure((0, 2, 3), weight=1)
        self.window.rowconfigure(1, weight=2)
        # self.window.grid_propagate(False)

        self.labels["task"].place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.canvas.grid(column=1, row=1)
        self.buttons["start"].grid(column=0, row=2, sticky=tk.NE)
        self.labels["loop"].grid(column=1, row=2, sticky=tk.N)
        self.buttons["reset"].grid(column=2, row=2, sticky=tk.NW)
