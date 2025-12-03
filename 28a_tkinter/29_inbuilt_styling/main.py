import tkinter as tk
from tkinter import font, ttk  # noqa (F401)

# window
window = tk.Tk()
window.title("Inbuilt Styling")
window.geometry("400x300")

# print(font.families())

# styles
style = ttk.Style()
# print(style.theme_names()) # outdated style
# style.theme_use("classic") # win95 theme
style.configure(
    "new.TButton",
    foreground="green",
    font=("FiraCode Nerd Font Mono", 18),
)
style.map(
    "new.TButton",
    foreground=[("pressed", "red"), ("disabled", "yellow")],
    background=[("pressed", "green"), ("disabled", "blue")],
)
style.configure(
    "exercise.TFrame",
    background="pink",
)


# frame
exercise_frame = ttk.Frame(
    window,
    width=200,
    height=150,
    style="exercise.TFrame",
)


# widgets
label = ttk.Label(
    window,
    text="A label\nAnd then type another line",
    background="red",
    foreground="white",
    font=("FiraCode Nerd Font Mono", 18),
    justify="right",
)
button = ttk.Button(
    window,
    text="button",
    style="new.TButton",
    # state="disabled",
)


# layouts
label.pack()
button.pack()
exercise_frame.pack()


# run
window.mainloop()
