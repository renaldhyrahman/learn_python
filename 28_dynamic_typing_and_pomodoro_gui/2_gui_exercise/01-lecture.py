import tkinter as tk
from tkinter import ttk

# root
root = tk.Tk()
root.title("GUI Lecture 1")
root.geometry("400x600")

# widgets
label1 = ttk.Label(root, text="First label", background="red")
label2 = ttk.Label(root, text="Label 2", background="blue")
label3 = ttk.Label(root, text="Last of the labels", background="green")
button = ttk.Button(root, text="Button")

# layout
label1.pack(side="top", expand=True, fill="both")
label2.pack(side="top", fill="x")
label3.pack(side="top")
button.pack(side="top", expand=True, fill="y")

# run
root.mainloop()
