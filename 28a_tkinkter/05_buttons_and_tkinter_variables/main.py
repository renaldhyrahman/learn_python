import tkinter as tk
from tkinter import ttk


# commands
def button_func():
    print("button pressed")


def exercise_func():
    print(exercise_check_var.get())
    exercise_check_var.set(False)


# window
window = tk.Tk()
window.title("Button and variable")
window.geometry("600x400")


# variables
button_str = tk.StringVar(value="button")
checkbox1_var = tk.BooleanVar(value=False)
checkbox2_var = tk.IntVar(value=10)
radio_var = tk.StringVar()

exercise_radio_var = tk.StringVar()
exercise_check_var = tk.BooleanVar()


# widgets
button = ttk.Button(
    master=window,
    textvariable=button_str,
    command=button_func,
)
checkbox1 = ttk.Checkbutton(
    master=window,
    text="checkbox 1",
    variable=checkbox1_var,
    command=lambda: print(
        f"checkbox1 = {checkbox1_var.get()}, "
        f"type = {type(checkbox1_var.get())}"
    ),
)
checkbox2 = ttk.Checkbutton(
    master=window,
    text="checkbox 2",
    variable=checkbox2_var,
    onvalue=5,
    offvalue=10,
    command=lambda: print(
        f"checkbox2 = {checkbox2_var.get()}, "
        f"type = {type(checkbox2_var.get())}"
    ),
)
radio1 = ttk.Radiobutton(
    master=window,
    text="Radio button 1",
    value="radio 1",  # default value is 0
    variable=radio_var,
    command=lambda: print(radio_var.get()),
)
radio2 = ttk.Radiobutton(
    master=window,
    text="Radio button 1",
    value=2,  # default value is 0
    variable=radio_var,
    command=lambda: print(radio_var.get()),
)

exercise_frame = ttk.Frame(window)
exercise_radio_frame = ttk.Frame(exercise_frame)
exercise_radio1 = ttk.Radiobutton(
    exercise_radio_frame,
    text="A",
    value="A",
    variable=exercise_radio_var,
    command=exercise_func,
)
exercise_radio2 = ttk.Radiobutton(
    exercise_radio_frame,
    text="B",
    value="B",
    variable=exercise_radio_var,
    command=exercise_func,
)
exercise_checkbox = ttk.Checkbutton(
    exercise_frame,
    text="exercise",
    variable=exercise_check_var,
    command=lambda: print(exercise_radio_var.get()),
)


# layout
button.pack()
checkbox1.pack()
checkbox2.pack()
radio1.pack()
radio2.pack()

exercise_frame.pack(pady=20)
exercise_radio_frame.pack()
exercise_radio1.pack(side="left")
exercise_radio2.pack(side="left")
exercise_checkbox.pack()


# run
window.mainloop()
