import tkinter as tk
from tkinter import ttk


class Segment(ttk.Frame):
    def __init__(
        self,
        parent: tk.Tk,
        label_text: str,
        button_text: str,
        nested_button_text: str = "",
    ):
        super().__init__(master=parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.pack(expand=True, fill="both", padx=10, pady=10)
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nsew")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew")
        self.create_widget(button_text=nested_button_text).grid(
            row=0, column=2, sticky="nsew"
        )

    def create_widget(self, button_text: str):
        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(expand=True, fill="both")
        ttk.Button(frame, text=button_text).pack(expand=True, fill="both")
        return frame
