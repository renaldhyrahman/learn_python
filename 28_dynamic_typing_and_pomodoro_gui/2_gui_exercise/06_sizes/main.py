import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Exercise 6 - Size")
root.geometry("400x300")

label1 = ttk.Label(root, text="Label 1", background="green")
label2 = ttk.Label(root, text="Label 2", background="red", width=50)

# label1.pack()
# label2.pack(fill="x")

root.columnconfigure((0, 1), weight=1, uniform="a")
root.rowconfigure((0, 1), weight=1, uniform="a")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky="nsew")

root.mainloop()
