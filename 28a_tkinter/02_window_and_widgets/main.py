import tkinter as tk
from tkinter import ttk


# commands
def button_func():
    print("a button was pressed")


# window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")


# widgets
text = tk.Text(master=window)

label = ttk.Label(master=window, text="This is a test")
entry = ttk.Entry(master=window)
button = ttk.Button(master=window, text="A Button", command=button_func)
exercise_frame = ttk.Frame(master=window)
exercise_label = ttk.Label(master=exercise_frame, text="My label")
exercise_button = ttk.Button(
    master=exercise_frame,
    text="Exercise button",
    command=lambda: print("Hello"),
)


# layout
label.pack()
text.pack()
entry.pack()
exercise_frame.pack()
exercise_label.pack(side="left")
exercise_button.pack(side="left")
button.pack()


# run
window.mainloop()
