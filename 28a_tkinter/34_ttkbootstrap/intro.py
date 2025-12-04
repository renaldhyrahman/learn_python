import ttkbootstrap as ttk
from ttkbootstrap import constants as c

"""
docs:
https://ttkbootstrap.readthedocs.io/en/latest/
"""

# window
window = ttk.Window(themename="journal")
window.title("ttk bootstrap intro")
window.geometry("400x300")

label = ttk.Label(window, text="Label")
label.pack(pady=10)

button1 = ttk.Button(window, text="Red", bootstyle=(c.DANGER, c.OUTLINE))
button1.pack(pady=10)

button2 = ttk.Button(window, text="Warning", bootstyle=c.WARNING)
button2.pack(pady=10)

button3 = ttk.Button(window, text="Green", bootstyle=c.SUCCESS)
button3.pack(pady=10)

# run
window.mainloop()
