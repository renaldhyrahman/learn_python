import customtkinter as ctk


class Entry(ctk.CTkFrame):
    def __init__(
        self,
        parent: ctk.CTkFrame,
        label_text: str,
        label_bg_color: str,
        button_text,
    ):
        super().__init__(parent)
        self.label1 = ctk.CTkLabel(
            self, text=label_text, fg_color=label_bg_color
        )
        self.button1 = ctk.CTkButton(self, text=button_text)

    def build_layout(self):
        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)
        self.label1.pack(expand=True, fill="both")
        self.button1.pack(expand=True, fill="both", pady=10)
