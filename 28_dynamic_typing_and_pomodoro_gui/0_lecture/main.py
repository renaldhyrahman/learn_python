import tkinter as t

from config import Color, FilePath, Font, Size, Time  # noqa (F401)

# init
root = t.Tk()
canvas = t.Canvas(root)
labels = {}

# configs
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=Color.YELLOW.value)
canvas.config(
    width=200, height=224, bg=Color.YELLOW.value, highlightthickness=0
)
bg_img = t.PhotoImage(file=FilePath.BG_IMAGE.value)
canvas.create_image(100, 112, image=bg_img)
canvas.create_text(
    101, 140, text="00:00", fill=Color.WHITE.value, font=Font.TIMER.value
)


# layout
canvas.pack()


# run
root.mainloop()
