import ttkbootstrap as ttk
from ttkbootstrap import constants as c
from ttkbootstrap.widgets.dateentry import DateEntry
from ttkbootstrap.widgets.floodgauge import Floodgauge
from ttkbootstrap.widgets.scrolled import ScrolledFrame
from ttkbootstrap.widgets.toast import ToastNotification
from ttkbootstrap.widgets.tooltip import ToolTip

# window
window = ttk.Window(themename="darkly")
window.title("Extra Widgets")


# scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill="both")
for i in range(100):
    _frame = ttk.Frame(scroll_frame)
    _frame.pack(pady=10)
    ttk.Label(_frame, text=f"Label: {i+1}").pack(side="left", padx=5)
    ttk.Button(_frame, text=f"Button: {i+1}").pack(side="left")


# toast
toast = ToastNotification(
    title="This is a message tittle",
    message="This is actual message",
    duration=3000,
    bootstyle=(c.WARNING),  # Does not support outline
    # position=(padx,pady,starting_pos)
    position=(50, 100, "ne"),
)
ttk.Button(
    window,
    text="show toast",
    command=toast.show_toast,
).pack(pady=20)


# tooltip
button = ttk.Button(window, text="tooltip button", bootstyle=c.WARNING)
button.pack(pady=20)
ToolTip(button, text="This does something", bootstyle=(c.INFO, c.INVERSE))


# calendar
calendar = DateEntry(window)
calendar.pack(pady=20)
ttk.Button(
    window,
    text="get calender date",
    command=lambda: print(calendar.entry.get()),
).pack()


# progress
progress_int = ttk.IntVar(value=50)
progress = Floodgauge(
    window,
    variable=progress_int,
    bootstyle=c.DANGER,
    mask="progress {}%",
)
progress.pack(pady=20, fill=c.X)
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()


# Meter
meter_double = ttk.DoubleVar(value=29)
meter = ttk.Meter(
    amounttotal=100,
    amountused=meter_double.get(),
    subtext="miles per hour",
    interactive=True,
    bootstyle=c.DANGER,
)
meter.step(1.0)
meter.pack()


# Sandbox Pomodoro Project
# timer_input = 62 * 60
timer_input = 10
meter_timer_int = ttk.IntVar(value=timer_input)
stopwatch = None


def mount_pause():
    start_button.pack_forget()
    next_button.pack_forget()
    pause_button.pack(side="left", padx=2)
    next_button.pack(side="left", padx=2)


def mount_start():
    pause_button.pack_forget()
    next_button.pack_forget()
    start_button.pack(side="left", padx=2)
    next_button.pack(side="left", padx=2)


def start():
    countdown(meter_timer_int.get())
    mount_pause()


def pause():
    global stopwatch
    window.after_cancel(stopwatch)
    stopwatch = None
    mount_start()
    start_button.configure(text="Resume")


def stop():
    global stopwatch
    if stopwatch is not None:
        window.after_cancel(stopwatch)
        stopwatch = None
    update_time(timer_input)
    mount_start()
    start_button.configure(text="Start")


def countdown(time_left: int):
    global stopwatch
    if time_left == 0:
        stop()
        return
    update_time(time_left)
    stopwatch = window.after(1000, countdown, time_left - 1)


def format_time(time_left: int):
    mins, secs = divmod(time_left, 60)
    if mins < 60:
        hours = 0
    else:
        hours, mins = divmod(mins, 60)
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)


def update_time(time_left: int):
    time_string = format_time(time_left)
    meter_timer_int.set(time_left)
    meter_timer.configure(
        amountused=meter_timer_int.get(), subtext=time_string
    )


frame_timer = ttk.Frame(window)
meter_timer = ttk.Meter(
    frame_timer,
    metersize=250,
    amountmin=timer_input,
    amounttotal=0,
    amountused=meter_timer_int.get(),
    showtext=False,
    subtext=format_time(timer_input),
    subtextfont="size 28",
    metertype=c.FULL,
    interactive=False,
    bootstyle=c.LIGHT,
)

frame_buttons = ttk.Frame(frame_timer)
start_button = ttk.Button(
    frame_buttons,
    text="Start",
    command=start,
)
stop_button = ttk.Button(
    frame_buttons,
    text="Stop",
    command=stop,
)
pause_button = ttk.Button(
    frame_buttons,
    text="Pause",
    command=pause,
)
next_button = ttk.Button(
    frame_buttons,
    text="Next",
)

frame_timer.pack()
meter_timer.pack()
frame_buttons.place(relx=0.5, rely=0.65, anchor="center")
stop_button.pack(side="left", padx=2)
mount_start()


# run
window.mainloop()
