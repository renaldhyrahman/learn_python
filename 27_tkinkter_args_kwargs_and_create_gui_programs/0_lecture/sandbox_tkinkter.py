# from tkinter import *
import tkinter as t

window = t.Tk()

# ##################  Window

window.title("My first GUI Program")
window.minsize(width=640, height=480)

# ##################  Label

# my_label = t.Label(text="I am a label")  # Create components
# my_label.pack()  # Place it into of window and x-axis centered

my_label = t.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Another new Text")

# ##################  Button

clicked = 0


def button_clicked():
    # my_label.config(text="You clicked the button")
    global clicked
    clicked += 1
    button.config(text=f"clicked {clicked}")


button = t.Button(text="Click me", command=button_clicked)
# button.pack()

# ##################  Entry (input)

entry = t.Entry(width=10)
entry.insert("end", string="Placeholder")
# entry.pack()

# ##################  Textbox

textbox = t.Text(height=5, width=30)
# Put cursor in textbox.
textbox.focus()
textbox.insert("end", "Example of multi-line text entry.")
# Get current value in textbox at line 1, index 0 (`"1.0"`)
print(textbox.get("1.0", "end"))
# textbox.pack()

# ##################  Spinbox


def spinbox_used():
    # Gets the current value in spinbox.
    print(spinbox.get())


spinbox = t.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# ##################  Scale


def scale_used(value):
    print(value)


scale = t.Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# ##################  Checkbutton (checkbox)


def checkbutton_used():
    # prints truthy (1 or 0)
    print(checked_state.get())


checked_state = t.IntVar()
checkbutton = t.Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
# checked_state.get() # ???
# checkbutton.pack()

# ##################  Radiobutton


def radio_used():
    print(radio_state.get())


radio_state = t.IntVar()
radiobutton1 = t.Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = t.Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
# radiobutton1.pack()
# radiobutton2.pack()

# ##################  Listbox


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = t.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind(sequence="<<ListboxSelect>>", func=listbox_used)
# listbox.pack()

# ##################


def entry_submit():
    my_label.config(text=entry.get())
    # clear entry
    entry.delete(0, "end")


entry_button = t.Button(text="submit", command=entry_submit)
# entry_button.pack()

# ################## Assemble

my_label.pack()
button.pack()
entry.pack()
textbox.pack()
spinbox.pack()
scale.pack()
checkbutton.pack()
radiobutton1.pack()
radiobutton2.pack()
listbox.pack()

entry_button.pack()

window.mainloop()
