import tkinter as tk
from random import choice as rc
from tkinter import ttk


# commands
def item_select(_):
    # print(table.selection())  # ('I00B',) ('I007', 'I00B', 'I010')
    for el in table.selection():
        # print(table.item(el))
        """bash
        {
          'text': '',
          'image': '',
          'values': ['Lisa', 'Thomson', 'LThomson@mail.com'],
          'open': 0,
          'tags': '',
        }
        """
        print(table.item(el)["values"])


def delete_items(_):
    print("delete")
    for el in table.selection():
        table.delete(el)


# window
window = tk.Tk()
window.title("Treeview")
window.geometry("600x400")

# data
first_name = [
    "Bob",
    "Maria",
    "Alex",
    "James",
    "Susan",
    "Henry",
    "Lisa",
    "Anna",
]
last_name = [
    "Smith",
    "Brown",
    "Wilson",
    "Thomson",
    "Cook",
    "Taylor",
    "Walker",
    "Clark",
]


# treeview
table = ttk.Treeview(
    window,
    columns=("first", "last", "email"),
    show="headings",
)
table.heading("first", text="First name")
table.heading("last", text="Surname")
table.heading("email", text="Email")
# insert values into table
# table.insert(parent="", index=0, values=("Jhon", "Doe", "JhonDoe@mail.com"))
for i in range(100):
    _fname = rc(first_name)
    _sname = rc(last_name)
    _email = f"{_fname[0]}{_sname}@mail.com"
    table.insert(parent="", index=i, values=(_fname, _sname, _email))
table.insert(parent="", index=tk.END, values=("XXXXX", "YYYYY", "ZZZZZ"))


# events
table.bind("<<TreeviewSelect>>", item_select)
table.bind("<Delete>", delete_items)


# layout
table.pack(expand=True, fill="both")


# run
window.mainloop()
