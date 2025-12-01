import tkinter as tk
from tkinter import ttk

from .frame_entry import Entry


class Main(ttk.Frame):
    def __init__(self, parent: tk):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = Entry(
            self,
            label_text="Entry 1",
            label_bg_color="red",
            button_text="Button 1",
        )
        self.frame2 = Entry(
            self,
            label_text="Entry 2",
            label_bg_color="blue",
            button_text="Button 2",
        )

    def build_layout(self):
        self.frame1.build_layout()
        self.frame2.build_layout()
