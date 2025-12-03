import tkinter as tk
from tkinter import ttk

# docs
"""
https://www.tutorialspoint.com/python/tk_menu.htm
"""


# window
window = tk.Tk()
window.title("Menu")
window.geometry("600x400")


# menu
menubar = tk.Menu(window)

# variables
help_check_var = tk.StringVar(value="off")

# sub menu
file_menu = tk.Menu(menubar, tearoff=False)  # default `tearoff=True`
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_separator()
menubar.add_cascade(label="File", menu=file_menu)

# another sub menu
help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(
    label="Help entry", command=lambda: print(help_check_var.get())
)
help_menu.add_checkbutton(
    label="check", onvalue="on", offvalue="off", variable=help_check_var
)
menubar.add_cascade(label="Help", menu=help_menu)

# menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="entry 1", command=lambda: print("test 1"))
button_sub_menu.add_checkbutton(label="checkbutton 1")
# menu_button.configure(menu=button_sub_menu)
menu_button["menu"] = button_sub_menu


# exercise
exercise_menu = tk.Menu(menubar, tearoff=False)
exercise_menu.add_command(label="Outside sub")

exercise_sub_menu = tk.Menu(exercise_menu, tearoff=False)
exercise_sub_menu.add_command(
    label="Inside sub", command=lambda: print("nested menu")
)

exercise_menu.add_cascade(label="Sub", menu=exercise_sub_menu)
menubar.add_cascade(label="Exercise", menu=exercise_menu)


# mount menu into window
window.configure(menu=menubar)


# layouts
menu_button.pack()


# run
window.mainloop()
