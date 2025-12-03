import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# commands


# window
window = tk.Tk()
window.title("Sliders")
# window.geometry("300x300")


# variables
scale_var = tk.DoubleVar(value=15)
exercise_var = tk.DoubleVar(value=0)


# widgets
scale = ttk.Scale(
    window,
    from_=0,
    to=25,
    length=300,
    orient="horizontal",  # by default orient is 'horizontal'
    variable=scale_var,
    # command=lambda v: print(
    #     scale_var.get()
    # ),  # by default value is 0 to 1.0 (float)
    command=lambda _: progress.stop(),
)

progress = ttk.Progressbar(
    window,
    variable=scale_var,
    maximum=25,
    mode="indeterminate",  # 'determinate' | 'indeterminate'
    length=400,
)
# progress.start(interval=1000)  # interval is in `ms`
# progress.stop()

scrolled_text = ScrolledText(window, width=100, height=5)

exercise_frame = ttk.Frame(window)
exercise_label = ttk.Label(
    exercise_frame,
    textvariable=exercise_var,
)
exercise_progress = ttk.Progressbar(
    exercise_frame,
    maximum=100,
    variable=exercise_var,
    orient="vertical",
    length=200,
)
exercise_scale = ttk.Scale(
    exercise_frame,
    from_=100,
    to=0,
    variable=exercise_var,
    orient="vertical",
    length=200,
)
exercise_progress.start()

# layouts
scale.pack()
progress.pack()
scrolled_text.pack()
exercise_frame.pack()
exercise_label.pack()
exercise_scale.pack(side="left")
exercise_progress.pack(side="left")


# run
window.mainloop()
