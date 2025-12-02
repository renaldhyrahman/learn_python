import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("GUI Exercise 7 - Stacking Order")
window.geometry("400x400")

label1 = ttk.Label(window, text="Label 1", background="green")
label2 = ttk.Label(window, text="Label 2", background="red")
label3 = ttk.Label(window, text="Label 3", background="orange")

# label1.lift()
# label2.lower()

button1 = ttk.Button(
    window,
    text="raise label 1",
    command=lambda: label1.tkraise(aboveThis=label2),
)
button2 = ttk.Button(
    window, text="raise label 2", command=lambda: label2.tkraise()
)
button3 = ttk.Button(
    window, text="raise label 3", command=lambda: label3.tkraise()
)

label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=75, y=80, width=100, height=100)
button1.place(rely=1, relx=0.8, anchor="se")
button2.place(rely=1, relx=1, anchor="se")
button3.place(rely=1, relx=0.6, anchor="se")


window.mainloop()
