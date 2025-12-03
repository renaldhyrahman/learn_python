import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Tab Widget")
window.geometry("600x400")


# notebook widgets
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

exercise_tab = ttk.Frame(notebook)
notebook.add(exercise_tab, text="Exercise")


# widgets
label1 = ttk.Label(tab1, text="Text in tab 1")
button1 = ttk.Button(tab1, text="button in tab 1")
label2 = ttk.Label(tab2, text="Text in tab 2")
entry2 = ttk.Entry(tab2)

exercise_label = ttk.Label(exercise_tab, text="Exercise label")
exercise_button_frame = ttk.Frame(exercise_tab)
exercise_button1 = ttk.Button(exercise_button_frame, text="button 1")
exercise_button2 = ttk.Button(exercise_button_frame, text="button 2")


# layouts
notebook.pack()
label1.pack()
button1.pack()
label2.pack()
entry2.pack()

exercise_label.pack()
exercise_button_frame.pack()
exercise_button1.pack(side="left")
exercise_button2.pack(side="left")


# run
window.mainloop()
