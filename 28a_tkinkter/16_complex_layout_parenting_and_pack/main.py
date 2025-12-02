import tkinter as tk
from tkinter import ttk

# root
root = tk.Tk()
root.title("GUI Exercise 3 - Frame")
root.geometry("400x600")


# top widget
frame_top = ttk.Frame(root)
label1 = ttk.Label(frame_top, text="First label", background="red")
label2 = ttk.Label(frame_top, text="Label 2", background="blue")
# mid widget
label3 = ttk.Label(root, text="Another label", background="green")
# bottom widget
frame_bottom = ttk.Frame(root)
label4 = ttk.Label(
    frame_bottom, text="Last of the labels", background="orange"
)
button1 = ttk.Button(frame_bottom, text="A Button")
button2 = ttk.Button(frame_bottom, text="Another Button")
# side buttons
frame_bottom_buttons = ttk.Frame(frame_bottom)
button3 = ttk.Button(frame_bottom_buttons, text="Button 3")
button4 = ttk.Button(frame_bottom_buttons, text="Button 4")
button5 = ttk.Button(frame_bottom_buttons, text="Button 5")


def layout_top():
    frame_top.pack(fill="both", expand=True)
    label1.pack(side="left", fill="both", expand=True)
    label2.pack(side="left", fill="both", expand=True)


def layout_mid():
    label3.pack(expand=True)


def layout_bottom():
    frame_bottom.pack(fill="both", expand=True, padx=20, pady=20)
    button1.pack(side="left", fill="both", expand=True)
    label4.pack(side="left", fill="both", expand=True)
    button2.pack(side="left", fill="both", expand=True)
    frame_bottom_buttons.pack(side="left", fill="both", expand=True)

    button3.pack(fill="both", expand=True)
    button4.pack(fill="both", expand=True)
    button5.pack(fill="both", expand=True)


def layout_build():
    layout_top()
    layout_mid()
    layout_bottom()


def run():
    layout_build()
    root.mainloop()


run()
