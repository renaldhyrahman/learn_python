import tkinter as tk

import constants as cons
from PIL import Image, ImageTk


def get_quote():
    pass
    # Write your code here.


window = tk.Tk()
window.title(cons.TITLE)
window.config(padx=cons.PADDING, pady=cons.PADDING)

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
text_quote = canvas.create_text(
    img_xcor,
    img_ycor,
    text="Kanye Quote Goes HERE",
    width=cons.TEXT_WIDTH,
    font=cons.TEXT_FONT,
    fill=cons.TEXT_COLOR,
)

# button
button_kanye = tk.Button(
    image=imgtk_kanye,
    highlightthickness=0,
    border=0,
    command=None,
)

# layout
canvas.grid(column=0, row=0)
button_kanye.grid(column=0, row=1)

# run
window.mainloop()
