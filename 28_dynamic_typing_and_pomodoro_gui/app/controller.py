import tkinter as tk

import app.constants as cons
from app.model import Model
from app.state import State
from app.view import View


class Controller:
    def __init__(self):
        self.stopwatch = None
        self.model = Model(
            commands={
                "start": self.countdown_start,
                "reset": self.countdown_stop,
            }
        )
        self.state = State(
            task=tk.StringVar(),
            counter_secs=tk.IntVar(value=0),
            max_loop=tk.IntVar(value=cons.Timer.LOOP.value),
            counter_loop=tk.IntVar(),
        )
        self.view = View(
            window=self.model.window,
            state=self.state,
            data_image=(
                self.model.image_tk,
                self.model.image_size,
            ),
            canvas=self.model.canvas,
            labels=self.model.labels,
            buttons=self.model.buttons,
            mode_idle=self.mode_idle,
        )

    def mode_idle(self):
        self.state.task.set("Idle")
        self.state.counter_secs.set(0)
        self.state.counter_loop.set(0)

    def mode_work(self):
        self.state.task.set("Work")
        self.state.counter_secs.set(cons.Timer.WORK.value)

    def mode_break(self):
        counter_loop = self.state.counter_loop
        counter_loop.set(counter_loop.get() + 1)
        if counter_loop.get() < self.state.max_loop.get():
            self.state.task.set("Short Break")
            self.state.counter_secs.set(cons.Timer.SHORT_BREAK.value)
        else:
            self.state.task.set("Long Break")
            self.state.counter_secs.set(cons.Timer.LONG_BREAK.value)

    def transition(self):
        task = self.state.task.get()
        transition_map = {
            "Idle": self.mode_work,
            "Work": self.mode_break,
            "Short Break": self.mode_work,
            "Long Break": self.mode_idle,
        }
        if task in transition_map:
            transition_map[task]()
            self.countdown_start()

    def countdown_stop(self):
        if self.stopwatch is None:
            return
        self.model.window.after_cancel(self.stopwatch)
        self.stopwatch = None
        self.mode_idle()

    def countdown_start(self):
        counter_secs = self.state.counter_secs
        if counter_secs.get() == 0:
            return self.transition()
        counter_secs.set(counter_secs.get() - 1)
        self.stopwatch = self.model.window.after(
            1000,
            self.countdown_start,
        )

    def run(self):
        self.model.window.mainloop()
