import tkinter as tk  # noqa (F401)
from random import choice, randint  # noqa (F401)
from tkinter import ttk  # noqa (F401)

# window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")


# # canvas
# canvas = tk.Canvas(
#     window,
#     bg="white",
#     scrollregion=(
#         0,
#         0,
#         2000,
#         5000,
#     ),  # scrollregion = (left, top, rigth, bottom)
# )
# for i in range(100):
#     _left = randint(0, 2000)
#     _top = randint(0, 5000)
#     _right = _left + randint(10, 500)
#     _bottom = _top + randint(10, 500)
#     _color = choice(("red", "green", "blue", "yellow", "orange"))
#     canvas.create_rectangle(_left, _top, _right, _bottom, fill=_color)
# canvas.create_line(0, 0, 2000, 5000, fill="green", width=10)

# # scorllbar
# scollbar_vertical = ttk.Scrollbar(
#     window,
#     orient="vertical",
#     command=canvas.yview,
# )
# scollbar_horizontal = ttk.Scrollbar(
#     window,
#     orient="horizontal",
#     command=canvas.xview,
# )

# canvas.configure(
#     yscrollcommand=scollbar_vertical.set,
#     xscrollcommand=scollbar_horizontal.set,
# )


# # binds
# canvas.bind(
#     "<MouseWheel>",
#     # canvas.yview_scroll(`amount`, `units`)
#     func=lambda e: canvas.yview_scroll(int(e.delta / 60 * -1), "units"),
# )
# canvas.bind(
#     "<Control-MouseWheel>",
#     func=lambda e: canvas.xview_scroll(int(e.delta / 60 * -1), "units"),
# )


# # layouts
# canvas.pack(expand=True, fill="both")
# scollbar_vertical.place(relx=1, rely=0, relheight=1, anchor="ne")
# scollbar_horizontal.place(relx=0, rely=1, relwidth=0.975, anchor="sw")


# text
# text = tk.Text(window)
# for i in range(1, 200):
#     text.insert(
#         index=f"{i}.0",
#         chars=f"text: {i}\n",
#     )  # index=1.0 => 1 be starting line and 0 be the character on that line
# text.pack(expand=True, fill="both")
# scollbar_text = ttk.Scrollbar(
#     window,
#     orient="vertical",
#     command=text.yview,
# )
# text.configure(yscrollcommand=scollbar_text.set)
# scollbar_text.place(relx=1, rely=0, relheight=1, anchor="ne")


# treeview
first_names = [
    "Bob",
    "Maria",
    "Alex",
    "James",
    "Susan",
    "Henry",
    "Lisa",
    "Anna",
]
last_names = [
    "Smith",
    "Brown",
    "Wilson",
    "Thomson",
    "Cook",
    "Taylor",
    "Walker",
    "Clark",
]
table = ttk.Treeview(window, columns=(1, 2), show="headings")
table.heading(1, text="First name")
table.heading(2, text="Last name")
for _ in range(100):
    table.insert(
        parent="",
        index=tk.END,
        values=(choice(first_names), choice(last_names)),
    )
table.pack(expand=True, fill="both")

scrollbar_table = ttk.Scrollbar(window, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor="ne")


# run
window.mainloop()
