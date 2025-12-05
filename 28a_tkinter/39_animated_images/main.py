import customtkinter as ctk
from animated_button import AnimatedButton

# from PIL import Image


def switch_theme():
    ctk.set_appearance_mode(switch_var.get())


# window
window = ctk.CTk()
window.title("Animations")
window.geometry("300x200")

# variables
star_black_path = "assets/black"
star_yellow_path = "assets/yellow"
heart_light_path = "assets/light"
heart_dark_path = "assets/dark"


# widgets
switch_var = ctk.StringVar(value="dark")
switch = ctk.CTkSwitch(
    window,
    text="Switch Theme",
    command=switch_theme,
    variable=switch_var,
    onvalue="light",
    offvalue="dark",
)

animated_button_star = AnimatedButton(
    parent=window,
    light_path=star_black_path,
    dark_path=star_yellow_path,
    button_text="Star button",
)
animated_button_heart = AnimatedButton(
    parent=window,
    light_path=heart_light_path,
    dark_path=heart_dark_path,
    button_text="Heart button",
    loop=True,
)


# layout
switch.place(relx=0, rely=0, anchor="nw")
animated_button_star.pack(expand=True)
animated_button_heart.pack(expand=True)

# run
window.mainloop()
