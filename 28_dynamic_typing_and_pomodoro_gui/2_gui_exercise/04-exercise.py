import tkinter as tk
from tkinter import ttk

# root
root = tk.Tk()
root.title("GUI Exercise 4 - Grid")
root.geometry("600x400")


# widgets
label1 = ttk.Label(root, text="Label 1", background="red")
label2 = ttk.Label(root, text="Label 2", background="blue")
label3 = ttk.Label(root, text="Label 3", background="green")
label4 = ttk.Label(root, text="Label 4", background="yellow")
button1 = ttk.Button(root, text="Button 1")
button2 = ttk.Button(root, text="Button 2")
entry = ttk.Entry(root)


# ########## Sandbox 1

# # define a grid (container)
# root.columnconfigure((0, 1, 2), weight=1)
# root.columnconfigure(3, weight=10)
# root.rowconfigure((0, 1, 2), weight=1)
# root.rowconfigure(3, weight=3)
# # place a widget
# label1.grid(row=0, column=0, sticky="nsew")
# label2.grid(row=1, column=1, rowspan=3, sticky="nsew")
# label3.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
# label4.grid(row=3, column=3, sticky="se")

# # ########## Sandbox 2

# root.columnconfigure((0, 1, 2), weight=1, uniform="a")
# root.rowconfigure(0, weight=1, uniform="a")

# label1.grid(row=0, column=0, sticky="nsew")
# label2.grid(row=0, column=2, sticky="nsew")

# ########## Sandbox 3

root.columnconfigure((0, 1, 2), weight=1, uniform="a")
root.columnconfigure(3, weight=2, uniform="a")
root.rowconfigure((0, 1, 2), weight=1, uniform="a")
root.rowconfigure(3, weight=3, uniform="a")

label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=1, column=1, rowspan=3, sticky="nsew")
label3.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
label4.grid(row=3, column=3, sticky="se")
button1.grid(row=0, column=3, sticky="nsew")
button2.grid(row=2, column=2, sticky="nsew")
entry.grid(row=2, column=3, rowspan=2, sticky="ew")


# run
root.mainloop()
