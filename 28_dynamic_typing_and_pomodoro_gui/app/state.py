import tkinter as tk
from dataclasses import dataclass


@dataclass
class State:
    task: tk.StringVar
    counter_secs: tk.IntVar
    max_loop: tk.IntVar
    counter_loop: tk.IntVar
