import tkinter as tk
from tkinter import constants as c
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageTk


def stretch_image(e):
    global resized_tk
    # size
    width = e.width
    height = e.height
    # print(f"w={width}, h={height}")

    # create an image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on canvas
    canvas.create_image(0, 0, image=resized_tk, anchor=c.NW)


def fill_image(e):
    global resized_tk

    # current ratio
    canvas_ratio = e.width / e.height

    # get coordinates
    if canvas_ratio > image_ratio:  # canvas is wider than image
        width = int(e.width)
        height = int(width / image_ratio)
    else:  # canvas is narrower than image
        height = int(e.height)
        width = int(height * image_ratio)
    resize_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resize_image)
    canvas.create_image(
        int(e.width / 2),
        int(e.height / 2),
        image=resized_tk,
        anchor=c.CENTER,
    )


def maintain_image_ratio(e):
    global resized_tk
    canvas_ratio = e.width / e.height
    if canvas_ratio > image_ratio:  # canvas is wider than image
        height = int(e.height)  # keep height if wider
        width = int(height * image_ratio)
    else:  # canvas is narrower than image
        width = int(e.width)  # keep width if narrow
        height = int(width / image_ratio)
    resize_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resize_image)
    canvas.create_image(
        int(e.width / 2),
        int(e.height / 2),
        image=resized_tk,
        anchor=c.CENTER,
    )


# window
window = tk.Tk()
window.title("Images")
window.geometry("600x400")


# frame
button_frame = ttk.Frame(window)


# import an image
image_original = Image.open("assets/raccoon.webp")
_img_witdh, _img_height = image_original.size
image_ratio = _img_witdh / _img_height
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open("assets/python_dark.webp").resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

# light_image have light bg, so image need to be dark (contrast reason)
img_ctk = ctk.CTkImage(
    light_image=Image.open("assets/python_dark.webp"),
    dark_image=Image.open("assets/python_light.webp"),
)


# widgets
# label_raccoon = ttk.Label(window, text="raccoon", image=image_tk)
# label_raccoon.pack()

button = ttk.Button(
    button_frame,
    text="    A button",
    image=python_dark_tk,
    compound=c.LEFT,
)

button_ctk = ctk.CTkButton(
    button_frame,
    text="    A button",
    image=img_ctk,
    compound=c.LEFT,
)

# canvas -> image
canvas = tk.Canvas(
    window,
    # bg="white",
    bd=0,
    highlightthickness=0,
    relief=c.RIDGE,
)
# canvas.bind("<Configure>", stretch_image)
# canvas.bind("<Configure>", fill_image)
canvas.bind("<Configure>", maintain_image_ratio)


# layout
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
window.rowconfigure(0, weight=1)
button_frame.grid(row=0, column=0, sticky=c.NSEW)
button.pack(pady=10)
button_ctk.pack(pady=10)
canvas.grid(row=0, column=1, columnspan=3, sticky=c.NSEW)


# run
window.mainloop()
