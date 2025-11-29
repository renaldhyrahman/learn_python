import tkinter as t

# ##################  Events


def button_event():
    print("clicked")
    my_label.config(text=entry.get())
    entry.delete(0, "end")
    entry.insert("end", string="Placeholder")


# ##################  Window


window = t.Tk()
window.title("My first GUI Program")
window.minsize(width=640, height=480)


# ##################  Label


my_label = t.Label(text="I am a label", font=("Arial", 24, "bold"))


# ##################  Button


button = t.Button(text="Click me", command=button_event)


# ##################  Entry (input)


entry = t.Entry(width=10)
entry.insert("end", string="Placeholder")


# ##################  Placement

# .pack():  Will always starts at the top and pack
#           any other widget below the prev one.
#           (side='left'), etc.
# .place(): Precise posioning, kind of css absolute position
# .grid() : Grid like css grid, can not be mixed with .pack()

# ######  PACK

# my_label.pack()
# button.pack()
# entry.pack()

# ######  Place

# my_label.place(x=0, y=0)  # (0,0) => top left
# my_label.place(x=100, y=0)
# button.pack()
# entry.pack()

# ######  Grid

my_label.grid(column=0, row=0)
# button.pack() # _tkinter.TclError: cannot use geometry manager pack inside
button.grid(column=1, row=1)
entry.grid(column=2, row=2)


window.mainloop()
