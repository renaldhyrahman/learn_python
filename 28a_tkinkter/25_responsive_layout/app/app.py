import tkinter as tk
from tkinter import ttk

from .responsive import SizeNotifier


class App(tk.Tk):
    def __init__(self, title: str, start_size: tuple[int, int]):
        super().__init__()
        self.title(title)
        self.geometry(f"{start_size[0]}x{start_size[1]}")
        self.frame = None
        self.create_and_pack_frame()

        SizeNotifier(
            self,
            {
                600: self.create_layout_md,
                300: self.create_layout_sm,
                1200: self.create_layout_lg,
            },
        )

    def create_and_pack_frame(self):
        if self.frame is not None:
            self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill="both")

    def create_layout_sm(self):
        self.create_and_pack_frame()
        ttk.Label(self.frame, text="Label 1", background="red").pack(
            expand=True, fill="both", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 2", background="green").pack(
            expand=True, fill="both", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 3", background="blue").pack(
            expand=True, fill="both", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 4", background="yellow").pack(
            expand=True, fill="both", padx=10, pady=5
        )

    def create_layout_md(self):
        self.create_and_pack_frame()
        self.frame.columnconfigure((0, 1), weight=1, uniform="a")
        self.frame.rowconfigure((0, 1), weight=1, uniform="a")
        ttk.Label(self.frame, text="Label 1", background="red").grid(
            column=0, row=0, sticky="nsew", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 2", background="green").grid(
            column=1, row=0, sticky="nsew", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 3", background="blue").grid(
            column=0, row=1, sticky="nsew", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 4", background="yellow").grid(
            column=1, row=1, sticky="nsew", padx=10, pady=5
        )

    def create_layout_lg(self):
        self.create_and_pack_frame()
        self.frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.frame.rowconfigure(0, weight=1)
        ttk.Label(self.frame, text="Label 1", background="red").grid(
            column=0, row=0, sticky="nsew", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 2", background="green").grid(
            column=1, row=0, sticky="nsew", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 3", background="blue").grid(
            column=2, row=0, sticky="nsew", padx=10, pady=5
        )
        ttk.Label(self.frame, text="Label 4", background="yellow").grid(
            column=3, row=0, sticky="nsew", padx=10, pady=5
        )

    def start(self):
        self.mainloop()
