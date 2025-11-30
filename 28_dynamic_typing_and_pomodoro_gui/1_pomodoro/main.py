import tkinter as t

from config import Color, FilePath, Font, Mode, Size, Time  # noqa (F401)

#
path = FilePath.BG_IMAGE.value
color_yellow = Color.YELLOW.value
color_green = Color.GREEN.value
color_white = Color.WHITE.value
color_red = Color.RED.value
size_screen = Size.SCREEN.value
font_title = Font.TITLE.value
font_timer = Font.TITLE.value
font_text = Font.TEXT.value
break_short = Time.SHORT_BREAK.value
break_long = Time.LONG_BREAK.value


# init
timer = 0
mode = 0
counter_break = 0
stopwatch = None


# setup_frames
root = t.Tk()
canvas = t.Canvas(root)
labels = {"heading": t.Label(root), "reps": t.Label(root)}
buttons = {"start": t.Button(root), "reset": t.Button(root)}


# setup_configs
root.title("Pomodoro")
root.config(padx=60, pady=20, bg=color_yellow)
canvas.config(
    width=200,
    height=223,
    bg=Color.YELLOW.value,
    highlightthickness=0,
)
labels["heading"].config(
    text="", fg=color_green, font=font_title, bg=color_yellow
)
img = t.PhotoImage(file=FilePath.BG_IMAGE.value)
img_bg = canvas.create_image(100, 111.5, image=img)
text_timer = canvas.create_text(
    100,
    130,
    text="00:00",
    fill=color_white,
    font=Font.TIMER.value,
)

buttons["start"].config(text="Start", font=font_text)
buttons["reset"].config(text="Reset", font=font_text)
labels["reps"].config(text="", font=font_title, bg=color_yellow)


# setup_layouts
# for n in range(5):
#     root.columnconfigure(n, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

labels["heading"].grid(row=0, column=1)
canvas.grid(row=1, column=1)
buttons["start"].grid(row=2, column=0)
buttons["reset"].grid(row=2, column=2)
labels["reps"].grid(row=3, column=1)


# utils
def format_time(time_left):
    mins, secs = divmod(time_left, 60)
    canvas.itemconfig(text_timer, text="{:02d}:{:02d}".format(mins, secs))


# handlers
def increase_reps(is_reset: bool = False):
    global counter_break
    if is_reset:
        counter_break = 0
        labels["reps"].config(text="")
        return
    counter_break += 1
    result = ""
    for _ in range(counter_break):
        result += "✔"
    labels["reps"].config(text=result)


def countdown(time_left):
    if time_left < 0:
        handler_start()
        return
    global stopwatch
    format_time(time_left)
    stopwatch = root.after(1000, countdown, time_left - 1)
    print(time_left)


def handler_reset():
    global timer
    global mode
    global stopwatch
    mode = Mode.LONG_BREAK.value
    timer = 0
    labels["heading"].config(text="Idle")
    canvas.itemconfig(text_timer, text="00:00")
    increase_reps(is_reset=True)
    if stopwatch is not None:
        root.after_cancel(stopwatch)
        stopwatch = None


def handler_start():
    global timer
    global mode
    print(f"Handler_Start, mode={mode}")
    mode_work = Mode.WORK.value
    mode_short_break = Mode.SHORT_BREAK.value
    mode_long_break = Mode.LONG_BREAK.value
    if mode == mode_short_break or mode == mode_long_break:
        mode = mode_work
        timer = Time.WORK.value
        labels["heading"].config(text="Work")
    elif mode == mode_work and counter_break < 3:
        increase_reps()
        mode = mode_short_break
        timer = Time.SHORT_BREAK.value
        labels["heading"].config(text="Break")
    else:
        increase_reps(is_reset=True)
        mode = mode_long_break
        timer = Time.LONG_BREAK.value
        labels["heading"].config(text="Break")
    countdown(timer)


# run
buttons["start"].config(command=handler_start)
buttons["reset"].config(command=handler_reset)
root.mainloop()
