# from tkinter import *
import tkinter as t

window = t.Tk()

# ##################  Window

window.title("My first GUI Program")
window.minsize(width=640, height=480)

# ##################  Label

# my_label = t.Label(text="I am a label")  # Create components
# my_label.pack()  # Place it into of window and x-axis centered

my_label = t.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Another new Text")

# ##################  Button

clicked = 0


def button_clicked():
    # my_label.config(text="You clicked the button")
    global clicked
    clicked += 1
    button.config(text=f"clicked {clicked}")


button = t.Button(text="Click me", command=button_clicked)
button.pack()

# ##################  Entry (input)

entry = t.Entry(width=10)
entry.pack()


def entry_submit():
    my_label.config(text=entry.get())
    # clear entry
    entry.delete(0, "end")


entry_button = t.Button(text="submit", command=entry_submit)
entry_button.pack()

# ##################

window.mainloop()
