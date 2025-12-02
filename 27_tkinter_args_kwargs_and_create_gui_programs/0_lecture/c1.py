import tkinter as t

window = t.Tk()
window.title("Layouting")
window.minsize(width=640, height=480)

# Padding
window.config(padx=20, pady=20)

label = t.Label(text="I am a label", font=("Arial", 24, "bold"))
label.config(padx=20, pady=20)
button1 = t.Button(text="Button 1")
button2 = t.Button(text="Button 2")
entry = t.Entry(width=20)
entry.insert("end", string="Placeholder")


# ##################  Placement

label.grid(column=0, row=0)
button1.grid(column=2, row=0)
button2.grid(column=1, row=1)
entry.grid(column=3, row=2)

window.mainloop()
