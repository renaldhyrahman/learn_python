import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Colors")
window.geometry("400x300")


# widgets
ttk.Label(window, background="red").pack(expand=True, fill="both")
ttk.Label(window, background="#08F").pack(expand=True, fill="both")
ttk.Label(window, background="#4fc296").pack(expand=True, fill="both")
ttk.Label(window, background="#955").pack(expand=True, fill="both")


# run
window.mainloop()
