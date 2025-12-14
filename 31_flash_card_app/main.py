import random as r
import tkinter as tk
from dataclasses import dataclass

import constants as cons
import pandas
from PIL import Image, ImageTk

# ######################      State     ######################


@dataclass
class State:
    language: tk.StringVar
    word: tk.StringVar


# ######################     Helpers    ######################


def fetch_df():
    try:
        df = pandas.read_csv(cons.Path.DATA.value)
    except FileNotFoundError:
        return
    else:
        languages = df.columns.to_list()
        words = df.to_dict(orient="records")
        return (languages, words)


# ######################      Logic     ######################


def display_card(is_front: bool):
    if is_front:
        image = imgtk_card_front
    else:
        image = imgtk_card_back
    canvas.itemconfig(c_img, image=image)


def display_random_word():
    languange, words = data

    random_languange = r.choice(languange)
    random_words = r.choice(words)

    state.language.set(random_languange)
    state.word.set(random_words[random_languange])


# ######################    Handlers    ######################


def on_known():
    print("on_known")
    display_random_word()


def on_unknown():
    print("on_unknown")
    display_random_word()


# ######################    Observer    ######################


def obs_state_word(*args):
    canvas.itemconfigure(c_text_language, text=state.language.get())
    canvas.itemconfigure(c_text_word, text=state.word.get())


# ######################    UI Setup    ######################


# window/root
window = tk.Tk()
window.title(cons.TITLE)
window.configure(
    bg=cons.Color.BG_GREEN.value,
    padx=cons.Size.PADDING.value,
    pady=cons.Size.PADDING.value,
)
window.resizable(0, 0)

# state and variables
state = State(
    language=tk.StringVar(),
    word=tk.StringVar(),
)
data = None

# attach observer/listener
state.word.trace_add("write", obs_state_word)

# images
img_card_front = Image.open(cons.Path.IMG_CARD_FRONT.value)
img_card_back = Image.open(cons.Path.IMG_CARD_BACK.value)
img_check = Image.open(cons.Path.IMG_RIGHT.value)
img_cross = Image.open(cons.Path.IMG_WRONG.value)

imgtk_card_front = ImageTk.PhotoImage(img_card_front)
imgtk_card_back = ImageTk.PhotoImage(img_card_back)
imgtk_check = ImageTk.PhotoImage(img_check)
imgtk_cross = ImageTk.PhotoImage(img_cross)

# canvas
canvas = tk.Canvas(
    window,
    width=cons.Size.CANVAS.value[0],
    height=cons.Size.CANVAS.value[1],
    bg=cons.Color.BG_GREEN.value,
    highlightthickness=0,
)
c_img = canvas.create_image(cons.Coordinate.IMAGE.value)
c_text_language = canvas.create_text(
    cons.Coordinate.LANGUAGE.value,
    text=state.language.get(),
    font=cons.Font.LANGUAGE.value,
)
c_text_word = canvas.create_text(
    cons.Coordinate.WORD.value,
    text=state.word.get(),
    font=cons.Font.WORD.value,
)

# buttons
button_known = tk.Button(
    window,
    image=imgtk_check,
    highlightthickness=0,
    border=0,
    command=on_known,
)
button_unknown = tk.Button(
    window,
    image=imgtk_cross,
    highlightthickness=0,
    border=0,
    command=on_unknown,
)

# layout
canvas.grid(column=0, row=0, columnspan=2)
button_unknown.grid(column=0, row=1)
button_known.grid(column=1, row=1)


# ######################     Start     ######################

try:
    data = fetch_df()
    if data is None:
        raise FileNotFoundError
except FileNotFoundError:
    print("Data is not found.")
else:
    display_random_word()
    display_card(True)
    window.mainloop()
