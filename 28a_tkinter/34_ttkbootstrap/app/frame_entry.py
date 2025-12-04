import ttkbootstrap as ttk


class Entry(ttk.Frame):
    def __init__(
        self,
        parent: ttk.Frame,
        label_text: str,
        label_bg_color: str,
        button_text: str,
        button_color: str,
    ):
        super().__init__(parent)
        self.label1 = ttk.Label(
            self, text=label_text, background=label_bg_color
        )
        self.button1 = ttk.Button(
            self, text=button_text, bootstyle=button_color
        )

    def build_layout(self):
        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)
        self.label1.pack(expand=True, fill="both")
        self.button1.pack(expand=True, fill="both", pady=10)
