from tkinter import ttk


class Entry(ttk.Frame):
    def __init__(
        self, parent: ttk, label_text: str, label_bg_color: str, button_text
    ):
        super().__init__(parent)
        self.label1 = ttk.Label(
            self, text=label_text, background=label_bg_color
        )
        self.button1 = ttk.Button(self, text=button_text)

    def build_layout(self):
        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)
        self.label1.pack(expand=True, fill="both")
        self.button1.pack(expand=True, fill="both", pady=10)
