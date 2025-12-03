import tkinter as tk
from tkinter import ttk


# commands
def button_submit():
    print(exercise_var.get())
    exercise_var.set("")


# windows
window = tk.Tk()
window.title("Frames and Parenting")
window.geometry("600x400")


# variables
exercise_var = tk.StringVar()


# frame (container)
frame = ttk.Frame(
    window,
    width=200,
    height=200,
    borderwidth=10,
    relief=tk.GROOVE,  # default `relief=tk.FLAT`
)
frame.pack_propagate(False)  # default `True`

exercise_frame = ttk.Frame(window)


# widgets
label = ttk.Label(frame, text="Label in frame")
button = ttk.Button(frame, text="Button in a frame")
label2 = ttk.Label(window, text="Label outside frame")

exercise_label = ttk.Label(exercise_frame, text="Name: ")
exercise_entry = ttk.Entry(exercise_frame, textvariable=exercise_var)
exercise_button = ttk.Button(
    exercise_frame, text="submit", command=button_submit
)


# layout
frame.pack(side=tk.LEFT)
label.pack()
button.pack()
label2.pack(side=tk.LEFT)
exercise_frame.pack(side=tk.LEFT, padx=10)
exercise_label.pack(side=tk.LEFT)
exercise_entry.pack(side=tk.LEFT)
exercise_button.pack(side=tk.LEFT)


# run
window.mainloop()
