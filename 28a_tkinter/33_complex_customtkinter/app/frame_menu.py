import customtkinter as ctk


class Menu(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.button1 = ctk.CTkButton(self, text="Button 1")
        self.button2 = ctk.CTkButton(self, text="Button 2")
        self.button3 = ctk.CTkButton(self, text="Button 3")
        self.slider1 = ctk.CTkSlider(self, orientation="vertical", width=20)
        self.slider2 = ctk.CTkSlider(self, orientation="vertical", width=20)
        self.toogle_frame = ctk.CTkFrame(self)
        self.toogle1 = ctk.CTkCheckBox(self.toogle_frame, text="check 1")
        self.toogle2 = ctk.CTkCheckBox(self.toogle_frame, text="check 2")
        self.entry = ctk.CTkEntry(self)

    def build_layout(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.button1.grid(
            row=0, column=0, sticky="nswe", columnspan=2, padx=1, pady=1
        )
        self.button2.grid(row=0, column=2, sticky="nswe", padx=1, pady=1)
        self.button3.grid(
            row=1, column=0, sticky="nswe", columnspan=3, padx=1, pady=1
        )
        self.slider1.grid(row=2, column=0, rowspan=2, sticky="ns", pady=20)
        self.slider2.grid(row=2, column=2, rowspan=2, sticky="ns", pady=20)
        self.toogle_frame.grid(row=4, column=0, sticky="we", columnspan=3)
        # self.toogle_frame.place(relx=0.5, rely=0.9, anchor="center")
        self.toogle1.pack(side="left", expand=True)
        self.toogle2.pack(side="left", expand=True)
        self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")
