import tkinter as tk
from tkinter import ttk


# commands
def button_func():
    print(string_var.get())
    string_var.set("button pressed")


# window
window = tk.Tk()
window.title("Tkinkter Variables")
window.geometry("200x200")


# tkinter variable
string_var = tk.StringVar(
    value="start value"
)  # StringVar, IntVar, DoubleVar, BooleanVar
exercise_var = tk.StringVar(value="text")


# widgets
label = ttk.Label(master=window, textvariable=string_var)
entry = ttk.Entry(master=window, textvariable=string_var)
button = ttk.Button(master=window, text="button", command=button_func)
entry2 = ttk.Entry(master=window, textvariable=string_var)
exercise_entry1 = tk.Entry(master=window, textvariable=exercise_var)
exercise_entry2 = tk.Entry(master=window, textvariable=exercise_var)
exercise_label = tk.Label(master=window, textvariable=exercise_var)


# layout
label.pack()
entry.pack()
button.pack()
entry2.pack()
exercise_entry1.pack()
exercise_label.pack()
exercise_entry2.pack()


# run
window.mainloop()
