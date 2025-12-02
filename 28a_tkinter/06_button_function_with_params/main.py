import tkinter as tk
from tkinter import ttk


# commands
def button_func(string_var: tk.StringVar):
    print(string_var.get())
    string_var.set("")
    entry.focus()


# window
window = tk.Tk()
window.title("buttons, function and argument")


# variables
entry_str = tk.StringVar()


# widgets
entry = ttk.Entry(window, textvariable=entry_str)
button = ttk.Button(
    window,
    text="button",
    command=lambda: button_func(entry_str),
)


# layout
entry.pack()
button.pack()


# run
entry.focus()
window.mainloop()
