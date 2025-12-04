import ttkbootstrap as ttk
from ttkbootstrap import constants as c

from .frame_entry import Entry


class Main(ttk.Frame):
    def __init__(self, parent: ttk.Window):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = Entry(
            self,
            label_text="Entry 1",
            label_bg_color="red",
            button_text="Button 1",
            button_color=(c.OUTLINE, c.PRIMARY),
        )
        self.frame2 = Entry(
            self,
            label_text="Entry 2",
            label_bg_color="blue",
            button_text="Button 2",
            button_color=(c.OUTLINE, c.SECONDARY),
        )

    def build_layout(self):
        self.frame1.build_layout()
        self.frame2.build_layout()
