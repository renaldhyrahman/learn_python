import tkinter as tk
from tkinter import ttk

from .frame_segment import Segment


class App(tk.Tk):
    def __init__(self, title: str, min_size: tuple[str, str]):
        super().__init__()
        self.title(title)
        self.geometry(f"{min_size[0]}x{min_size[1]}")
        self.minsize(min_size[0], min_size[1])

    # def create_widgets(self):
    #     Segment(self, "label", "button")
    #     Segment(self, "test", "click")
    #     Segment(self, "hello", "world")
    #     Segment(self, "bye", "launch")
    #     Segment(self, "last one", "exit")

    @staticmethod
    def create_segment(parent: tk.Tk, label_text: str, button_text: str):
        frame = ttk.Frame(parent)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
        # frame.pack(expand=True, fill="both", padx=10, pady=10)
        ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew")
        ttk.Button(frame, text=button_text).grid(
            row=0, column=1, sticky="nsew"
        )
        return frame

    # # class Approach
    # def start(self):
    #     self.create_widgets()
    #     self.mainloop()

    # # funtional Approach
    # def start(self):
    #     self.create_segment(self, "label", "button").pack(
    #         expand=True, fill="both", padx=10, pady=10
    #     )
    #     self.create_segment(self, "test", "click").pack(
    #         expand=True, fill="both", padx=10, pady=10
    #     )
    #     self.create_segment(self, "hello", "world").pack(
    #         expand=True, fill="both", padx=10, pady=10
    #     )
    #     self.create_segment(self, "bye", "launch").pack(
    #         expand=True, fill="both", padx=10, pady=10
    #     )
    #     self.create_segment(self, "last one", "exit").pack(
    #         expand=True, fill="both", padx=10, pady=10
    #     )
    #     self.mainloop()

    # exercise
    def create_widgets(self):
        Segment(
            parent=self,
            label_text="label",
            button_text="button",
            nested_button_text="test",
        )
        Segment(
            parent=self,
            label_text="test",
            button_text="click",
            nested_button_text="something else",
        )
        Segment(
            parent=self,
            label_text="hello",
            button_text="world",
            nested_button_text="123",
        )
        Segment(
            parent=self,
            label_text="bye",
            button_text="launch",
            nested_button_text="",
        )
        Segment(
            parent=self,
            label_text="last one",
            button_text="exit",
            nested_button_text="end",
        )

    def start(self):
        self.create_widgets()
        self.mainloop()
