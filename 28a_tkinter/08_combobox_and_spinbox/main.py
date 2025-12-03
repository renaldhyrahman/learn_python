import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Combo and spin")
window.geometry("600x400")

# variables
combo_items = ("Ice cream", "Pizza", "Broccoli")
food_string = tk.StringVar(value=combo_items[0])
spin_int = tk.IntVar(value=12)
exercise_spin_values = ("A", "B", "C", "D", "E")
exercise_spin_var = tk.StringVar(value=exercise_spin_values[0])


# widgets
combo = ttk.Combobox(
    window,
    # values=combo_items,
    textvariable=food_string,
)
# combo.configure(values=combo_items)
combo["values"] = combo_items
combo_label = ttk.Label(window, text="a label")

spin = ttk.Spinbox(
    window,
    from_=3,
    to=20,
    increment=3,
    textvariable=spin_int,
    command=lambda: print(f"an arrow was pressed, value={spin_int.get()}"),
)
# spin["value"] = (1, 2, 3, 4, 5)
exercise_spin = ttk.Spinbox(
    window,
    values=exercise_spin_values,
    textvariable=exercise_spin_var,
    # command=lambda: print(f"{exercise_spin_var.get()}"),
)


# events
combo.bind(
    "<<ComboboxSelected>>",
    lambda e: combo_label.configure(
        text=f"Selected value: {food_string.get()}"
    ),
)
spin.bind("<<Increment>>", lambda e: print("up"))
spin.bind("<<Decrement>>", lambda e: print("down"))
exercise_spin.bind("<<Decrement>>", lambda e: print(exercise_spin_var.get()))


# layouts
combo.pack()
combo_label.pack()
spin.pack()
exercise_spin.pack()


# run
window.mainloop()
