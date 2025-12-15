import tkinter as tk

import constants as cons
import requests
from PIL import Image, ImageTk


def obs_quotes(*args):
    canvas.itemconfig(canvas_text, text=quotes_var.get())


def get_quote():
    res = requests.get(cons.API)
    res.raise_for_status()
    quote = res.json()["quote"]
    quotes_var.set(quote)


# window
window = tk.Tk()
window.title(cons.TITLE)
window.config(padx=cons.PADDING, pady=cons.PADDING)

# state
quotes_var = tk.StringVar()

# observer
quotes_var.trace_add("write", obs_quotes)

# images
img_bg = Image.open(cons.IMG_BACKGROUND)
img_bg_width, img_bg_height = img_bg.size
imgtk_bg = ImageTk.PhotoImage(img_bg)
img_kanye = Image.open(cons.IMG_KANYE)
imgtk_kanye = ImageTk.PhotoImage(img_kanye)

# canvas
canvas = tk.Canvas(width=img_bg_width, height=img_bg_height)
img_xcor = img_bg_width / 2
img_ycor = img_bg_height / 2
canvas.create_image(img_xcor, img_ycor, image=imgtk_bg)
canvas_text = canvas.create_text(
    img_xcor,
    img_ycor,
    width=cons.TEXT_WIDTH,
    font=cons.TEXT_FONT,
    fill=cons.TEXT_COLOR,
)

# button
button_kanye = tk.Button(
    image=imgtk_kanye,
    highlightthickness=0,
    border=0,
    command=get_quote,
)

# layout
canvas.grid(column=0, row=0)
button_kanye.grid(column=0, row=1)

# run
get_quote()
window.mainloop()
