# from random import choice

import customtkinter as ctk


class SlidePanel(ctk.CTkFrame):
    def __init__(
        self,
        parent: ctk.CTk | ctk.CTkFrame,
        start_pos: float,
        end_pos: float,
    ):
        super().__init__(parent)
        self.start_pos = start_pos + 0.01
        self.end_pos = end_pos - 0.01
        self.width = abs(start_pos - end_pos)

        # logic
        self.pos = self.start_pos
        self.is_visible = False

        # layout
        self.mount(self.start_pos)

    def mount(self, relx: float):
        self.place(
            relx=relx,
            rely=0.05,
            relwidth=self.width,
            relheight=0.9,
        )

    def animate(self):
        if self.is_visible:
            self.animate_backward()
        else:
            self.animate_forward()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.mount(self.pos)
            self.after(10, self.animate_forward)
        else:
            self.is_visible = True

    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.mount(self.pos)
            self.after(10, self.animate_backward)
        else:
            self.is_visible = False


def move_btn():
    global button_x
    button_x = round(button_x + 0.01, 2)
    button.place(relx=button_x, rely=0.5, anchor="center")

    # configure
    # colors = ["red", "yellow", "pink", "green", "blue", "black", "white"]
    # color = choice(colors)
    # button.configure(fg_color=color)


def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print(f"infinite, button_x={button_x}")
        window.after(1000, infinite_print)


def button_slide():
    move_btn()
    if button_x < 0.9:
        window.after(10, button_slide)


# window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")
ctk.set_appearance_mode("light")

# animated widget
animated_panel = SlidePanel(window, 1, 0.7)
ctk.CTkLabel(animated_panel, text="Label 1").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkLabel(animated_panel, text="Label 2").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkButton(animated_panel, text="Button", corner_radius=0).pack(
    expand=True, fill="both", pady=10
)
ctk.CTkTextbox(animated_panel, fg_color=("#dbdbdb", "#2b2b2b")).pack(
    expand=True, fill="both", pady=10
)

# button
button_x = 0.5
button = ctk.CTkButton(
    window,
    text="toggle sidebar",
    command=animated_panel.animate,
)
button.place(relx=button_x, rely=0.5, anchor="center")


# run
window.mainloop()
