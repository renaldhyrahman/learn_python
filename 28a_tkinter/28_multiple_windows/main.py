import tkinter as tk
from tkinter import messagebox, ttk

"""
docs:
https://docs.python.org/3/library/tkinter.messagebox.html
"""


class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Extra window")
        self.geometry("300x400")
        ttk.Label(self, text="A label").pack()
        ttk.Button(self, text="button").pack()
        ttk.Label(self, text="another label").pack(expand=True)


# commands
def ask_yes_no():
    # answer = messagebox.askquestion("Title", "Body")
    # print(answer)
    # messagebox.showinfo("Title", "some information")
    messagebox.showerror("Title", "some information")


def create_window():
    global extra_window
    extra_window = Extra()


def close_window():
    global extra_window
    extra_window.destroy()
    extra_window = None


# variable
extra_window = None


# window
window = tk.Tk()
window.title("Multiple Windows")
window.geometry("600x400")


# widgets
button1 = ttk.Button(window, text="open main window", command=create_window)
button2 = ttk.Button(window, text="close main window", command=close_window)
button3 = ttk.Button(window, text="create yes no window", command=ask_yes_no)


# layouts
button1.pack(expand=True)
button2.pack(expand=True)
button3.pack(expand=True)


# run
window.mainloop()
