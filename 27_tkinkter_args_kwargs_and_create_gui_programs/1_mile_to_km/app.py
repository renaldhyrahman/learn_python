import tkinter as t

import config as c


class App:
    def __init__(self):
        self.window = t.Tk()
        self.labels = {
            "info": t.Label(self.window),
            "text": t.Label(self.window),
            "input": t.Label(self.window),
            "output": t.Label(self.window),
            "result": t.Label(self.window),
        }
        self.entry = t.Entry(self.window)
        self.button_calc = t.Button(self.window)
        self.radio_state = t.IntVar()
        self.radiobuttons = {
            "input_miles": t.Radiobutton(self.window),
            "input_km": t.Radiobutton(self.window),
        }

    def boot(self):
        self.window.title(c.TITLE_WINDOW_1)
        self.window.config(padx=c.PADDING_WINDOW, pady=c.PADDING_WINDOW)
        self.labels["info"].config(text="", fg="red")
        self.labels["text"].config(text="is equal to")
        self.labels["input"].config(text="Miles")
        self.labels["output"].config(text="Km")
        self.labels["result"].config(text="0")
        for _, v in self.labels.items():
            v.config(pady=c.PADDING_EL, padx=c.PADDING_EL, font=c.FONT_TEXT)
        self.radiobuttons["input_miles"].config(
            text="Miles to Km",
            value=c.RADIO_MILES,
            pady=c.PADDING_EL,
            padx=c.PADDING_EL,
        )
        self.radiobuttons["input_km"].config(
            text="Km to Miles",
            value=c.RADIO_KM,
            pady=c.PADDING_EL,
            padx=c.PADDING_EL,
        )
        self.radio_state.set(c.RADIO_MILES)
        self.entry.config(width=c.WIDTH_ENTRY)
        self.button_calc.config(text="calculate")
        self.arrange()

    def arrange(self):
        self.labels["info"].grid(columnspan=3, row=0)
        self.radiobuttons["input_miles"].grid(column=0, row=1)
        self.radiobuttons["input_km"].grid(column=1, row=1)
        self.entry.grid(column=1, row=2)
        self.labels["input"].grid(column=2, row=2)
        self.labels["text"].grid(column=0, row=3)
        self.labels["result"].grid(column=1, row=3)
        self.labels["output"].grid(column=2, row=3)
        self.button_calc.grid(column=1, row=4)

    def h_reset_input(self):
        self.labels["result"].config(text="0")
        self.entry.delete(0, "end")

    def h_bad_request(self):
        self.labels["info"].config(text="Input must be a number")
        self.h_reset_input()

    def h_validate_input(self):
        try:
            return float(self.entry.get())
        except ValueError:
            self.h_bad_request()
            return

    def h_calculate(self):
        input_number = self.h_validate_input()
        if input_number is None:
            return
        if self.radio_state.get() == c.RADIO_MILES:
            return input_number * 1.60934
        return input_number / 1.60934

    def e_radio(self):
        if self.radio_state.get() == c.RADIO_MILES:
            self.window.title(c.TITLE_WINDOW_1)
            self.labels["input"].config(text="Miles")
            self.labels["output"].config(text="Km")
        else:
            self.window.title(c.TITLE_WINDOW_2)
            self.labels["input"].config(text="Km")
            self.labels["output"].config(text="Miles")
        self.h_reset_input()
        self.labels["info"].config(text="")

    def e_display_result(self):
        result = self.h_calculate()
        if result is None:
            return
        self.labels["result"].config(text=f"{round(result, 2)}")
        self.labels["info"].config(text="")

    def run(self):
        self.button_calc.config(command=self.e_display_result)
        for _, rb in self.radiobuttons.items():
            rb.config(variable=self.radio_state, command=self.e_radio)
        self.entry.focus()
        self.window.mainloop()
