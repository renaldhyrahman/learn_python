import ttkbootstrap as ttk

from .frame_main import Main
from .frame_menu import Menu


class App(ttk.Window):
    def __init__(self, title: str, min_size: tuple[int, int]):
        super().__init__(themename="journal")
        self.title(title)
        self.geometry(f"{min_size[0]}x{min_size[1]}")
        self.minsize(min_size[0], min_size[1])
        self.menu = Menu(self)
        self.main = Main(self)

    def build_layout(self):
        self.menu.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.menu.build_layout()
        self.main.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.main.build_layout()

    def start(self):
        self.build_layout()
        self.mainloop()
