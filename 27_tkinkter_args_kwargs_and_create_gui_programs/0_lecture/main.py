import tkinter as t

window = t.Tk()

# ##################  Window

window.title("My first GUI Program")
window.minsize(width=1366, height=768)

# ##################  Label

# my_label = t.Label(text="I am a label")  # Create components
# my_label.pack()  # Place it into of window and x-axis centered

my_label = t.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# ##################

window.mainloop()
