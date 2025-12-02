import tkinter as tk

import ttkbootstrap as ttk  # type: ignore

# from tkinter import ttk


# window = tk.Tk()
window = ttk.Window(themename="darkly")
window.title("Length Converter")
window.geometry("300x150")


# commands
def convert():
    miles_input = int(entry_int.get())
    km_output = miles_input * 1.60934
    output_str.set(f"{round(km_output, 2)}")


# widgets
title_label = ttk.Label(
    master=window, text="Miles to Kilometers", font="Calibri 24 bold"
)
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
input_entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(
    master=input_frame,
    text="Convert",
    command=convert,
)
output_str = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text="",
    font="Calibri 24",
    textvariable=output_str,
)


# layout
title_label.pack()
input_frame.pack(pady=10)
input_entry.pack(side="left", padx=10)
button.pack(side="left")
output_label.pack(pady=5)


# run
input_entry.focus()
window.mainloop()
