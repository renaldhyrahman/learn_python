import tkinter as tk

import app.constants as cons
from app.model import Model
from app.state import State
from app.view import View


class Controller:
    def __init__(self):
        self.countdown_id = None
        self.model = Model(
            commands={
                "start": self.countdown_start,
                "reset": self.countdown_stop,
            }
        )
        self.state = State(
            task=tk.StringVar(),
            counter_secs=tk.IntVar(value=0),
            max_loop=tk.IntVar(value=cons.Timer.MAX_LOOP.value[1]),
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
        secs = cons.Timer.IDLE.value[1] * 60
        self.state.task.set(cons.Timer.IDLE.name)
        self.state.counter_secs.set(secs)
        self.state.counter_loop.set(0)

    def mode_work(self):
        secs = cons.Timer.WORK.value[1] * 60
        self.state.task.set(cons.Timer.WORK.name)
        self.state.counter_secs.set(secs)

    def mode_break(self):
        counter_loop = self.state.counter_loop
        counter_loop.set(counter_loop.get() + 1)
        if counter_loop.get() < self.state.max_loop.get():
            secs = cons.Timer.SHORT_BREAK.value[1] * 60
            self.state.task.set(cons.Timer.SHORT_BREAK.name)
            self.state.counter_secs.set(secs)
        else:
            secs = cons.Timer.LONG_BREAK.value[1] * 60
            self.state.task.set(cons.Timer.LONG_BREAK.name)
            self.state.counter_secs.set(secs)

    def transition(self):
        task = self.state.task.get()
        next_state_map = {
            cons.Timer.IDLE.name: self.mode_work,
            cons.Timer.WORK.name: self.mode_break,
            cons.Timer.SHORT_BREAK.name: self.mode_work,
            cons.Timer.LONG_BREAK.name: self.mode_idle,
        }
        if task in next_state_map:
            next_state_map[task]()
            self.countdown_start()

    def countdown_stop(self):
        if self.countdown_id is None:
            return
        self.model.after_cancel(self.countdown_id)
        self.countdown_id = None
        self.mode_idle()

    def countdown_start(self):
        counter_secs = self.state.counter_secs
        if counter_secs.get() == 0:
            return self.transition()
        counter_secs.set(counter_secs.get() - 1)
        self.countdown_id = self.model.after(
            1000,
            self.countdown_start,
        )

    def run(self):
        self.model.window.mainloop()
