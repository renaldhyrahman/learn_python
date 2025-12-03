"""
docs:
https://github.com/TomSchimansky/CustomTkinter
"""

# import tkinter as tk

import customtkinter as ctk

# from tkinter import ttk


# commands
def toggle_theme():
    mode = ctk.get_appearance_mode()
    new_mode = "dark" if mode == "Light" else "light"
    ctk.set_appearance_mode(new_mode)


# window
window = ctk.CTk()
window.title("customtkinter app")
window.geometry("600x400")

# widgets
string_var = ctk.StringVar(value="a custom string")
label = ctk.CTkLabel(
    window,
    text="A ctk label",
    fg_color=("blue", "red"),
    text_color=("black", "white"),
    corner_radius=10,
    textvariable=string_var,
)
label.pack()
button = ctk.CTkButton(
    window,
    text="ctk button",
    fg_color="#FF0",
    text_color="#000",
    hover_color="#AA0",
    command=toggle_theme,
)
button.pack()

frame = ctk.CTkFrame(window)
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)

switch = ctk.CTkSwitch(
    window,
    text="Exercise Switch",
    fg_color="red",
    progress_color="white",
    corner_radius=1,
    border_width=3,
    border_color="blue",
    button_color="yellow",
)
switch.pack()


# run
window.mainloop()
