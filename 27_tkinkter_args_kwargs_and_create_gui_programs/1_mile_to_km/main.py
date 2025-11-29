import tkinter as t

import config as c

# ######  Event


def reset_input():
    label_result.config(text="0")
    entry.delete(0, "end")


def bad_request():
    label_info.config(text="Input must be a number")
    reset_input()


def e_radio():
    if radio_state.get() == 1:
        window.title(c.TITLE_WINDOW_1)
        label_input.config(text="Miles")
        label_output.config(text="Km")
    else:
        window.title(c.TITLE_WINDOW_2)
        label_input.config(text="Km")
        label_output.config(text="Miles")
    reset_input()
    label_info.config(text="")


def e_calculate():
    try:
        input_number = float(entry.get())
    except ValueError:
        bad_request()
        return
    if radio_state.get() == 1:
        result = input_number * 1.60934
    else:
        result = input_number / 1.60934
    label_result.config(text=f"{round(result, 2)}")
    label_info.config(text="")


# ######  Window

window = t.Tk()
window.title(c.TITLE_WINDOW_1)
# window.minsize()

# ######  Components

label_info = t.Label(window, text="", font=c.FONT_TEXT)
label_text = t.Label(window, text="is equal to", font=c.FONT_TEXT)
label_input = t.Label(window, text="Miles", font=c.FONT_TEXT)
label_output = t.Label(window, text="Km", font=c.FONT_TEXT)
label_result = t.Label(window, text="0", font=c.FONT_TEXT)
entry = t.Entry(window, width=c.WIDTH_ENTRY)
button_calc = t.Button(window, text="calculate", command=e_calculate)
radio_state = t.IntVar()
radiobutton_1 = t.Radiobutton(
    window, text="Miles to Km", value=1, variable=radio_state, command=e_radio
)
radiobutton_2 = t.Radiobutton(
    window, text="Km to Miles", value=2, variable=radio_state, command=e_radio
)

entry.focus()

# ######  Configs

window.config(padx=c.PADDING_WINDOW, pady=c.PADDING_WINDOW)
label_info.config(fg="red")
radiobutton_1.config(pady=c.PADDING_EL, padx=c.PADDING_EL)
radiobutton_2.config(pady=c.PADDING_EL, padx=c.PADDING_EL)
label_input.config(pady=c.PADDING_EL, padx=c.PADDING_EL)
label_output.config(pady=c.PADDING_EL, padx=c.PADDING_EL)
radio_state.set(1)

# ######  Layout

label_info.grid(columnspan=3, row=0)
radiobutton_1.grid(column=0, row=1)
radiobutton_2.grid(column=1, row=1)
entry.grid(column=1, row=2)
label_input.grid(column=2, row=2)
label_text.grid(column=0, row=3)
label_result.grid(column=1, row=3)
label_output.grid(column=2, row=3)
button_calc.grid(column=1, row=4)

window.mainloop()
