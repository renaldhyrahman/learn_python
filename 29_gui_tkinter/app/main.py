import csv
import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox as msgbox

import app.constants as cons
from PIL import Image, ImageTk


@dataclass
class State:
    website: tk.StringVar
    email: tk.StringVar
    password: tk.StringVar


class App:
    def __init__(self):
        self.boot()

    def boot(self):
        self.setup_root()
        self.state = State(
            website=tk.StringVar(),
            email=tk.StringVar(),
            password=tk.StringVar(),
        )
        self.load_assets()
        self.setup_widgets()

        self.build_layout()

    def setup_root(self):
        self.root = tk.Tk()
        self.root.title(cons.TITLE)
        self.root.config(
            padx=cons.Size.PADDING.value,
            pady=cons.Size.PADDING.value,
        )

    def setup_widgets(self):
        self.setup_canvas()
        self.setup_label()
        self.setup_entry()
        self.setup_buttons()

    def load_assets(self):
        image = Image.open(cons.PATH_IMG)
        self.asset_img = ImageTk.PhotoImage(image)

    def setup_canvas(self):
        size_canvas = cons.Size.CANVAS.value
        self.canvas = tk.Canvas(
            self.root,
            width=size_canvas,
            height=size_canvas,
            highlightthickness=0,
        )

        img_xcor = size_canvas / 2
        img_ycor = size_canvas / 2
        self.canvas.create_image(img_xcor, img_ycor, image=self.asset_img)

    def setup_label(self):
        self.label_website = tk.Label(
            self.root,
            text="Website",
            font=cons.FONT_TEXT,
        )
        self.label_email = tk.Label(
            self.root,
            text="Email/Username",
            font=cons.FONT_TEXT,
        )
        self.label_password = tk.Label(
            self.root,
            text="Password",
            font=cons.FONT_TEXT,
        )

    def setup_entry(self):
        self.entry_website = tk.Entry(
            self.root,
            width=cons.Size.WIDTH_MD.value,
            font=cons.FONT_TEXT,
            textvariable=self.state.website,
        )
        self.entry_email = tk.Entry(
            self.root,
            width=cons.Size.WIDTH_MD.value,
            font=cons.FONT_TEXT,
            textvariable=self.state.email,
        )
        self.entry_password = tk.Entry(
            self.root,
            width=cons.Size.WIDTH_SM.value,
            font=cons.FONT_TEXT,
            textvariable=self.state.password,
        )

    def setup_buttons(self):
        self.button_generate = tk.Button(
            self.root,
            text="Generate Password",
            font=cons.FONT_TEXT,
            highlightthickness=0,
        )
        self.button_add = tk.Button(
            self.root,
            text="Add",
            width=cons.Size.WIDTH_LG.value,
            font=cons.FONT_TEXT,
            command=self.on_add,
            highlightthickness=0,
        )

    def reset_entry(self):
        self.state.website.set("")
        self.state.password.set("")

    def dialogue_missing_entry(self, message: str):
        msgbox.showinfo(
            title="Missing data",
            message=message,
        )

    def validate_entry(self):
        missing_list = []
        website = self.state.website.get().strip()
        if not len(website):
            missing_list.append("website")
        email = self.state.email.get().strip()
        if not len(email):
            missing_list.append("email")
        password = self.state.password.get().strip()
        if not len(password):
            missing_list.append("password")
        if len(missing_list):
            message = ""
            for missing in missing_list:
                message += f"{missing.capitalize()} is required."
                if len(missing_list) > 1:
                    message += "\n"
            self.dialogue_missing_entry(message)
            return []
        return [website, email, password]

    def on_add(self):
        entries = self.validate_entry()
        if not len(entries):
            return
        website, email, password = entries
        is_ok = msgbox.askokcancel(
            title=website,
            message="Is it ok to save?\n"
            f"email: {email}\n"
            f"password: {password}",
        )
        if not is_ok:
            return
        self.save_file((website, email, password))

    def validate_save_file(self, data: tuple[str, str, str]):
        try:
            with open(cons.PATH_SAVEFILE, "r", newline="") as f:
                reader = csv.reader(f)
                heading = next(reader)
                if heading != list(cons.FIELDNAMES):
                    raise ValueError
                return True
        except (FileNotFoundError, StopIteration, ValueError):
            return False

    def save_file(self, data: tuple[str, str, str]):
        is_valid_save_file = self.validate_save_file(data)
        if not is_valid_save_file:
            self.create_new_file(data)
        else:
            self.update_save_file(data)
        self.reset_entry()

    def create_new_file(self, data: tuple[str, str, str]):
        with open(cons.PATH_SAVEFILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(cons.FIELDNAMES)
            writer.writerow(data)

    def update_save_file(self, data: tuple[str, str, str]):
        with open(cons.PATH_SAVEFILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def build_layout(self):
        self.canvas.grid(column=0, row=0, columnspan=3)

        self.label_website.grid(column=0, row=1)
        self.entry_website.grid(
            column=1,
            row=1,
            columnspan=2,
            sticky=tk.W,
        )

        self.label_email.grid(
            column=0,
            row=2,
        )
        self.entry_email.grid(
            column=1,
            row=2,
            columnspan=2,
            sticky=tk.W,
        )

        self.label_password.grid(
            column=0,
            row=3,
        )
        self.entry_password.grid(
            column=1,
            row=3,
            sticky=tk.W,
        )
        self.button_generate.grid(
            column=2,
            row=3,
            sticky=tk.W,
        )

        self.button_add.grid(
            column=1,
            row=4,
            columnspan=2,
            sticky=tk.W,
        )

    def run(self):
        # debug
        self.debug()

        self.label_website.focus()
        self.root.mainloop()

    def debug(self):
        self.entry_website.insert(tk.END, "FooBar")
        self.entry_email.insert(tk.END, "jhon@doe.com")
        self.entry_password.insert(tk.END, "password")
