import json
import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox as msgbox

import constants as cons
import pyperclip
from helpers import generate_password
from PIL import Image, ImageTk

# ######################       State     ######################


@dataclass
class State:
    website: tk.StringVar
    email: tk.StringVar
    pwd: tk.StringVar


# ######################     Handlers     ######################


def reset_entry():
    state.website.set("")
    state.pwd.set("")


def on_search():
    website = state.website.get()
    try:
        data = read_savefile()
        if data is None:
            raise FileNotFoundError
        result = data[website]
    except KeyError as msg:
        msgbox.showerror(title="Not Found", message=f"{msg} is not found.")
    except FileNotFoundError:
        msgbox.showerror(title="Error", message="No Data File Found.")
    else:
        email = result["email"]
        pwd = result["password"]
        pyperclip.copy(pwd)
        state.email.set(email)
        state.pwd.set(pwd)
        msgbox.showinfo(
            title=website,
            message=f"Email: {email}\nPassword: {pwd}",
        )


def on_get_pwd(state: tk.StringVar):
    pwd = generate_password()
    state.set(pwd)
    pyperclip.copy(pwd)


def read_savefile():
    try:
        with open(cons.PATH_SAVEFILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def on_add(website: str, email: str, pwd: str):
    if not len(website) or not len(pwd):
        return msgbox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty.",
        )
    is_ok = msgbox.askokcancel(
        title=website,
        message="These are the details entered:\n"
        f"Email: {email}\n"
        f"Password: {pwd}\n"
        "Is it ok to save?",
    )

    if not is_ok:
        return

    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    try:
        data = read_savefile()
        if data is None:
            raise FileNotFoundError
        data.update(new_data)
    except FileNotFoundError:
        data = new_data

    with open(cons.PATH_SAVEFILE, "w") as f:
        json.dump(data, f, indent=4)

    reset_entry()


# ######################    UI Setup    ######################


# window/root
window = tk.Tk()
window.title(cons.TITLE)
window.config(padx=cons.Size.PADDING.value, pady=cons.Size.PADDING.value)

# state
state = State(
    website=tk.StringVar(),
    email=tk.StringVar(),
    pwd=tk.StringVar(),
)

# canvas
canvas_height = cons.Size.CANVAS.value
canvas_width = cons.Size.CANVAS.value
canvas = tk.Canvas(window, height=canvas_height, width=canvas_width)
logo_img = Image.open(cons.PATH_IMG)
logo_imgtk = ImageTk.PhotoImage(logo_img)
logo_xcor = canvas_width / 2
logo_ycor = canvas_height / 2
canvas.create_image(logo_xcor, logo_ycor, image=logo_imgtk)

# labels
website_label = tk.Label(
    window,
    text="Website",
    font=cons.FONT_TEXT,
)
email_label = tk.Label(
    window,
    text="Email",
    font=cons.FONT_TEXT,
)
pwd_label = tk.Label(
    window,
    text="Password",
    font=cons.FONT_TEXT,
)

# entries
website_entry = tk.Entry(font=cons.FONT_TEXT, textvariable=state.website)
email_entry = tk.Entry(font=cons.FONT_TEXT, textvariable=state.email)
pwd_entry = tk.Entry(font=cons.FONT_TEXT, textvariable=state.pwd)

# buttons
search_button = tk.Button(
    text="Search",
    font=cons.FONT_TEXT,
    command=on_search,
)
pwd_button = tk.Button(
    text="Generate Password",
    font=cons.FONT_TEXT,
    command=lambda: on_get_pwd(state.pwd),
)
add_button = tk.Button(
    text="Add",
    width=cons.Size.WIDTH_LG.value,
    font=cons.FONT_TEXT,
    command=lambda: on_add(
        website=state.website.get(),
        email=state.email.get(),
        pwd=state.pwd.get(),
    ),
)

# layout
canvas.grid(column=0, row=0, columnspan=3)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
pwd_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, sticky=tk.EW)
search_button.grid(column=2, row=1, sticky=tk.EW)
email_entry.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
pwd_entry.grid(column=1, row=3, sticky=tk.EW)
pwd_button.grid(column=2, row=3, sticky=tk.EW)
add_button.grid(column=1, row=4, columnspan=2)


state.email.set("foo@bar.com")
window.mainloop()
