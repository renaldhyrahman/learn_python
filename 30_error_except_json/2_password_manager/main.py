import csv
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
    password: tk.StringVar


# ######################     Handlers     ######################


def on_get_pwd(state: tk.StringVar):
    pwd = generate_password()
    state.set(pwd)
    pyperclip.copy(pwd)
    return pwd


def on_add(website: str, email: str, password: str):
    # website = website_entry.get()
    # email = email_entry.get()
    # password = password_entry.get()

    if not len(website) or not len(password):
        return msgbox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty.",
        )
    is_ok = msgbox.askokcancel(
        title=website,
        message="These are the details entered:\n"
        f"Email: {email}\n"
        f"Password: {password}\n"
        "Is it ok to save?",
    )
    if not is_ok:
        return
    with open(cons.PATH_SAVEFILE, "a") as f:
        writer = csv.writer(f)
        writer.writerow((website, email, password))
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
    password=tk.StringVar(),
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
website_text, email_text, password_text = cons.FIELDNAMES
website_label = tk.Label(window, text=website_text)
email_label = tk.Label(window, text=email_text)
password_label = tk.Label(window, text=password_text)

# entries
website_entry = tk.Entry(
    width=cons.Size.WIDTH_MD.value,
    textvariable=state.website,
)
email_entry = tk.Entry(
    width=cons.Size.WIDTH_MD.value,
    textvariable=state.email,
)
password_entry = tk.Entry(
    width=cons.Size.WIDTH_SM.value,
    textvariable=state.password,
)

# buttons
password_button = tk.Button(
    text="Generate Password",
    command=lambda: on_get_pwd(state.password),
)
add_button = tk.Button(
    text="Add",
    width=cons.Size.WIDTH_LG.value,
    command=lambda: on_add(
        website=state.website.get(),
        email=state.email.get(),
        password=state.password.get(),
    ),
)

# layout
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, columnspan=2, sticky=tk.W)
email_entry.grid(column=1, row=2, columnspan=2, sticky=tk.W)
password_entry.grid(column=1, row=3, sticky=tk.W)
password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)


def reset_entry():
    state.website.set("")
    state.password.set("")


state.email.set("foo@bar.com")
window.mainloop()
