import tkinter as tk
from tkinter import ttk

# list of events
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/


# commands
def get_pos(event):
    print(f"x={event.x}, y={event.y}")


# window
window = tk.Tk()
window.title("Event Binding")
window.geometry("600x500")


# widgets
textbox = tk.Text(window)
entry = ttk.Entry(window)
button = ttk.Button(window, text="button")


# layout
textbox.pack()
entry.pack()
button.pack()


# events
# window.bind("<Alt-KeyPress-a>", lambda event: print(event))
# button.bind("<Alt-KeyPress-a>", lambda event: print(event))
# window.bind("<Motion>", get_pos)
# textbox.bind("<Motion>", get_pos)
# window.bind("<KeyPress>", lambda event: print(f"keypress = {event.char}"))
entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("entry field was unselected"))
textbox.bind(
    "<Shift-MouseWheel>",
    lambda event: print(f"MouseWheel = {'up' if event.delta > 0 else 'down'}"),
)


# run
window.mainloop()
