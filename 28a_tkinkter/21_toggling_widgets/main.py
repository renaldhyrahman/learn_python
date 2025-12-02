import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Toggle Widget")
window.geometry("600x400")


# ##########  Place ##########


# def label_reveal(obj_label: ttk.Label):
#     obj_label.place(relx=0.5, rely=0.5, anchor="center")


# def label_toggle_place(obj_label: ttk.Label):
#     global is_label_visible
#     if is_label_visible:
#         obj_label.place_forget()
#         is_label_visible = False
#         return
#     label_reveal(obj_label)
#     is_label_visible = True


# is_label_visible = True
# button = ttk.Button(
#     window, text="toggle label", command=lambda: label_toggle_place(label)
# )
# button.place(x=10, y=10)

# label = ttk.Label(window, text="A label")
# label_reveal(label)


# # ##########  Grid ##########


# window.columnconfigure((0, 1), weight=1, uniform="a")
# window.rowconfigure(0, weight=1, uniform="a")


# def label_reveal(obj_label: ttk.Label):
#     obj_label.grid(column=1, row=0)


# def label_toggle_grid(obj_label: ttk.Label):
#     global is_label_visible
#     if is_label_visible:
#         obj_label.grid_forget()
#         is_label_visible = False
#         return
#     label_reveal(obj_label)
#     is_label_visible = True


# is_label_visible = True
# label = ttk.Label(window, text="A label")
# button = ttk.Button(
#     window, text="toggle label", command=lambda: label_toggle_grid(label)
# )

# button.grid(column=0, row=0)
# label_reveal(label)


# ##########  Pack ##########


# My solution


# def label_toggle_pack(obj_label: ttk.Label):
#     global is_label_visible
#     if is_label_visible:
#         obj_label.config(text="")
#         is_label_visible = False
#         return
#     obj_label.config(text="A label")
#     is_label_visible = True


# is_label_visible = True
# label = ttk.Label(window, text="A label")
# button = ttk.Button(
#     window, text="toggle label", command=lambda: label_toggle_pack(label)
# )

# label.pack(expand=True)
# button.pack()


# Alternative solution


def label_reveal(obj_label: ttk.Label):
    obj_label.pack(expand=True)


def label_toggle_pack(obj_label: ttk.Label):
    global is_label_visible
    if is_label_visible:
        obj_label.pack_forget()
        is_label_visible = False
        return
    label_reveal(obj_label)
    is_label_visible = True


is_label_visible = True
frame = ttk.Frame(window)
label = ttk.Label(frame, text="A label")
button = ttk.Button(
    window, text="toggle label", command=lambda: label_toggle_pack(label)
)

label_reveal(label)
button.pack()
frame.pack(expand=True, before=button)


# ##########  Run ##########

window.mainloop()
