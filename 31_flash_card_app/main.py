import os
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


def fetch_data():
    try:
        df = pandas.read_csv(cons.Path.RESULT.value)
    except FileNotFoundError:
        df = pandas.read_csv(cons.Path.DATA.value)
    finally:
        return df.to_dict(orient="records")


def update_csv():
    global data
    data_updated = [word for word in data if word != current_card]
    df_updated = pandas.DataFrame(data_updated)
    df_updated.to_csv(cons.Path.RESULT.value, index=False)
    data = data_updated


# ######################      Logic     ######################


def display_card(is_front: bool):
    if is_front:
        image = imgtk_card_front
        text_color = cons.Color.BLACK.value
    else:
        image = imgtk_card_back
        text_color = cons.Color.WHITE.value
    canvas.itemconfig(c_img, image=image)
    canvas.itemconfig(c_text_language, fill=text_color)
    canvas.itemconfig(c_text_word, fill=text_color)


def display_next_card():
    print(f"data_length = {len(data)}")
    global timer, current_card
    cancel_timer()
    language = cons.LANGUAGES[0]
    display_card(True)
    try:
        current_card = r.choice(data)
    except IndexError:
        return display_complete()
    state.language.set(language)
    state.word.set(current_card[language])
    timer = window.after(cons.DELAY * 1000, flip_card)


def display_complete():
    state.language.set("Congratulation!")
    state.word.set("You win.")
    button_unknown.config(state=tk.DISABLED)
    button_known.config(state=tk.DISABLED)
    os.remove(cons.Path.RESULT.value)


def flip_card():
    cancel_timer()
    language = cons.LANGUAGES[1]
    display_card(False)
    state.language.set(language)
    state.word.set(current_card[language])


def cancel_timer():
    global timer
    if timer is None:
        return
    window.after_cancel(timer)
    timer = None


# ######################    Handlers    ######################


def on_known():
    update_csv()
    display_next_card()


def on_unknown():
    display_next_card()


# ######################    Observer    ######################


def obs_state_word(*args):
    canvas.itemconfigure(c_text_language, text=state.language.get())
    canvas.itemconfigure(c_text_word, text=state.word.get())


# ######################    UI Setup    ######################


# window/root
window = tk.Tk()
window.title(cons.TITLE)
window.configure(
    bg=cons.Color.GREEN.value,
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
current_card = None
timer = None

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
    bg=cons.Color.GREEN.value,
    highlightthickness=0,
)
c_img = canvas.create_image(cons.Coordinate.IMAGE.value)
c_text_language = canvas.create_text(
    cons.Coordinate.LANGUAGE.value,
    font=cons.Font.LANGUAGE.value,
)
c_text_word = canvas.create_text(
    cons.Coordinate.WORD.value,
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


data = fetch_data()
display_next_card()
window.mainloop()
