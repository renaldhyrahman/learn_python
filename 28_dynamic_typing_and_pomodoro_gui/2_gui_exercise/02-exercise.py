import tkinter as tk
from tkinter import ttk

# root
root = tk.Tk()
root.title("GUI Exercise 2")
root.geometry("400x600")

# widgets
label1 = ttk.Label(root, text="First label", background="red")
label2 = ttk.Label(root, text="Label 2", background="blue")
label3 = ttk.Label(root, text="Last of the labels", background="green")
button = ttk.Button(root, text="Button")

# layout
label1.pack(side="top", expand=True, fill="both", padx=10, pady=10)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")

# run
root.mainloop()
