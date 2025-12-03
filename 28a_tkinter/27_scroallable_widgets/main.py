import tkinter as tk
from tkinter import ttk


class ListFrame(ttk.Frame):
    def __init__(
        self,
        parent: tk.Tk | ttk.Frame,
        text_data: list[tuple[str, str]],
        item_height: int,
    ):
        super().__init__(master=parent)
        self.pack(expand=True, fill="both")
        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height
        # canvas
        self.canvas = tk.Canvas(
            self,
            background="red",
            scrollregion=(0, 0, self.winfo_width(), self.list_height),
        )
        self.canvas.pack(expand=True, fill="both")
        # display frame
        self.frame = ttk.Frame(self)
        for i, item in enumerate(self.text_data):
            self.create_item(i, item).pack(
                expand=True, fill="both", padx=10, pady=4
            )
        # scrollbar
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # events
        self.bind("<Configure>", self.update_size)

    def update_size(self, e):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all(
                "<MouseWheel>",
                lambda e: self.canvas.yview_scroll(
                    int(e.delta / 60 * -1), "units"
                ),
            )
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
        else:
            height = self.winfo_height()
            self.canvas.unbind_all("<MouseWheel>")
            self.scrollbar.place_forget()
        self.canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor="nw",
            width=self.winfo_width(),
            height=height,
        )

    def create_item(self, index: int, item: tuple[str, str]):
        frame = ttk.Frame(self.frame)

        # grid layouts
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # widgets
        label_text, button_text = item
        ttk.Label(frame, text=f"#{index + 1}").grid(row=0, column=0)
        ttk.Label(frame, text=label_text).grid(row=0, column=1)
        ttk.Button(frame, text=button_text).grid(
            row=0, column=2, columnspan=3, sticky=tk.NSEW
        )

        return frame


# window
window = tk.Tk()
window.title("Scrolling")
window.geometry("500x400")

text_list = [
    ("label", "button"),
    ("thing", "click"),
    ("thrid", "something"),
    ("label1", "button"),
    ("label2", "button"),
    ("label3", "button"),
    ("label4", "button"),
]
list_frame = ListFrame(window, text_list, 100)

# run
window.mainloop()
