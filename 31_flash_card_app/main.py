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


# ######################    UI Setup    ######################


# window/root
window = tk.Tk()
window.title("Flash Card")
window.configure(bg=cons.Color.BG_GREEN.value, padx=50, pady=50)

# images
img_card_front = Image.open(cons.PATH_IMG_CARD_FRONT)
img_card_back = Image.open(cons.PATH_IMG_CARD_BACK)
img_right = Image.open(cons.PATH_IMG_RIGHT)
img_wrong = Image.open(cons.PATH_IMG_WRONG)

imgtk_card_front = ImageTk.PhotoImage(img_card_front)
imgtk_card_back = ImageTk.PhotoImage(img_card_back)
imgtk_right = ImageTk.PhotoImage(img_right)
imgtk_wrong = ImageTk.PhotoImage(img_wrong)


# canvas
canvas_width, canvas_height = img_card_front.size
canvas = tk.Canvas(
    window,
    width=canvas_width,
    height=canvas_height,
    bg=cons.Color.BG_GREEN.value,
    highlightthickness=0,
)
img_xcor = canvas_width / 2
img_ycor = canvas_height / 2
c_img = canvas.create_image(img_xcor, img_ycor)
c_text_language = canvas.create_text(
    img_xcor,
    150,
    font=cons.Font.LANGUAGE.value,
)
c_text_word = canvas.create_text(
    img_xcor,
    263,
    font=cons.Font.WORD.value,
)

# canvas config
canvas.itemconfig(c_text_language, text="French")
canvas.itemconfig(c_text_word, text="trouve")

# buttons
button_right = tk.Button(
    window,
    image=imgtk_right,
    highlightthickness=0,
    border=0,
    command=None,
)
button_wrong = tk.Button(
    window,
    image=imgtk_wrong,
    highlightthickness=0,
    border=0,
    command=None,
)

# layout
canvas.grid(column=0, row=0, columnspan=2)
button_wrong.grid(column=0, row=1)
button_right.grid(column=1, row=1)

# ######################     Start     ######################

display_card(True)
window.mainloop()
