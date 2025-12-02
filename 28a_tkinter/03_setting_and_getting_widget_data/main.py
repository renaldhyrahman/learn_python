import tkinter as tk
from tkinter import ttk


# commands
def button_func():
    label["text"] = entry.get()
    entry["state"] = "disabled"
    # print(label.configure())


def exercise_func():
    label["text"] = "Some text"
    entry["state"] = "enabled"


# window
window = tk.Tk()
window.title("Getting and Setting Widgets")
window.geometry("300x300")


# widgets
label = ttk.Label(master=window, text="Some Text")
entry = ttk.Entry(master=window)
button = ttk.Button(
    master=window,
    text="The button",
    command=button_func,
    # command=lambda: label.configure(text=entry.get()),
)
exercise_button = ttk.Button(
    master=window,
    text="Exercise button",
    command=exercise_func,
)


# layout
label.pack()
entry.pack()
button.pack()
exercise_button.pack()


# run
window.mainloop()
