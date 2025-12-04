import ttkbootstrap as ttk
from ttkbootstrap import constants as c


class Menu(ttk.Frame):
    def __init__(self, parent: ttk.Window):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.button1 = ttk.Button(
            self,
            text="Button 1",
            bootstyle=c.SUCCESS,
        )
        self.button2 = ttk.Button(
            self,
            text="Button 2",
            bootstyle=c.DANGER,
        )
        self.button3 = ttk.Button(
            self,
            text="Button 3",
            bootstyle=c.DARK,
        )
        self.slider1 = ttk.Scale(
            self,
            orient="vertical",
            bootstyle=c.WARNING,
        )
        self.slider2 = ttk.Scale(
            self,
            orient="vertical",
            bootstyle=c.INFO,
        )
        self.toogle_frame = ttk.Frame(self)
        self.toogle1 = ttk.Checkbutton(
            self.toogle_frame,
            text="check 1",
        )
        self.toogle2 = ttk.Checkbutton(
            self.toogle_frame,
            text="check 2",
        )
        self.entry = ttk.Entry(self)

    def build_layout(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.button1.grid(
            row=0,
            column=0,
            sticky="nswe",
            columnspan=2,
            padx=2,
            pady=2,
        )
        self.button2.grid(
            row=0,
            column=2,
            sticky="nswe",
            padx=2,
            pady=2,
        )
        self.button3.grid(
            row=1,
            column=0,
            sticky="nswe",
            columnspan=3,
            padx=2,
            pady=2,
        )
        self.slider1.grid(row=2, column=0, rowspan=2, sticky="nswe", pady=20)
        self.slider2.grid(row=2, column=2, rowspan=2, sticky="nswe", pady=20)
        self.toogle_frame.grid(row=4, column=0, sticky="nswe", columnspan=3)
        self.toogle1.pack(side="left", expand=True)
        self.toogle2.pack(side="left", expand=True)
        self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")
