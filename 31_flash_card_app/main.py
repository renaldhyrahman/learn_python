import tkinter as tk

import constants as cons
from PIL import Image, ImageTk

# ######################      State     ######################


# ######################    Handlers    ######################


def display_card(is_front: bool):
    if is_front:
        image = imgtk_card_front
    else:
        image = imgtk_card_back
    canvas.itemconfig(c_img, image=image)


def on_known():
    print("on_known")


def on_unknown():
    print("on_unknown")


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
    font=cons.Font.LANGUAGE.value,
)
c_text_word = canvas.create_text(
    cons.Coordinate.WORD.value,
    font=cons.Font.WORD.value,
)

# canvas config
canvas.itemconfig(c_text_language, text="French")
canvas.itemconfig(c_text_word, text="trouve")

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

display_card(True)
window.mainloop()
