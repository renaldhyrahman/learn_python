import tkinter as tk
from tkinter import ttk

# root
root = tk.Tk()
root.title("GUI Exercise 5 - Place")
root.geometry("400x600")


# widgets
label1 = ttk.Label(root, text="Label 1", background="red")
label2 = ttk.Label(root, text="Label 2", background="blue")
label3 = ttk.Label(root, text="Label 3", background="green")
button = ttk.Button(root, text="Button")


# ########## Sandbox 1

# # layout
# label1.place(x=300, y=100, width=100, height=200)
# label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
# label3.place(x=80, y=60, width=160, height=300)
# button.place(relx=1, rely=1, anchor="se")

# ########## Sandbox 2

# # frame
# frame = ttk.Frame(root)
# frame_label = ttk.Label(frame, text="Frame Label", background="yellow")
# frame_buton = ttk.Button(frame, text="Frame Button")

# # layout
# frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
# frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
# frame_buton.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# label1.place(x=300, y=100, width=100, height=200)
# label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
# label3.place(x=80, y=60, width=160, height=300)
# button.place(relx=1, rely=1, anchor="se")

# ########## Sandbox 3

frame = ttk.Frame(root)
frame_label = ttk.Label(frame, text="Frame Label", background="yellow")
frame_buton = ttk.Button(frame, text="Frame Button")
label_exercise = ttk.Label(root, text="Label exercise", background="orange")


frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_buton.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button.place(relx=1, rely=1, anchor="se")
label_exercise.place(
    relx=0.5, rely=0.5, relwidth=0.5, height=200, anchor="center"
)

# run
root.mainloop()
