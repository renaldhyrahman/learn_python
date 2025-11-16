import random as r
import turtle as t

import helpers as h

# Requirements:
# - 10x10 spots
# - Each dots has a diameter of 20, and 50 spacing between each of them


class Painter:
    """
    Handle canvas size, movements, draw a dot, and create hirst painting.

    Attributes:
        n_dots_x (int): Number of dots on x axis.
        n_dots_y (int): Number of dots on y axis.
        dot_diameter (int): Size for all dots.
        spacing (int): Space between each dots.

    Dependecies:
        fn `get_palette` (`helpers` module).
    """

    def __init__(
        self, n_dots_x: int, n_dots_y: int, dot_diameter: int, spacing: int
    ):
        self.turtle = t.Turtle()
        self.n_dots_x = n_dots_x
        self.n_dots_y = n_dots_y
        self.dot_diameter = dot_diameter
        self.spacing = spacing
        self.dot_radius = dot_diameter / 2
        self.distance = self.dot_radius + spacing
        self.set_color_palatte()
        self.screen = t.Screen()
        self.setup_canvas()

    def setup_canvas(self):
        width = self.distance * self.n_dots_x
        height = self.distance * self.n_dots_y
        self.screen.setup(
            width=width + (2 * self.spacing),
            height=height + (2 * self.spacing),
            startx=None,
            starty=None,
        )
        self.turtle.penup()
        self.turtle.setposition(width / -2, height / -2)

    def set_color_palatte(self):
        self.color_palatte = h.get_palette("image.jpg", 30)

    def draw_dot(self):
        self.turtle.pendown()
        self.turtle.dot(self.dot_diameter, r.choice(self.color_palatte))

    def move(self, direction: str, distance: int):
        self.turtle.penup()
        match direction:
            case "e":
                self.turtle.setheading(0)
            case "n":
                self.turtle.setheading(90)
            case "w":
                self.turtle.setheading(180)
            case "s":
                self.turtle.setheading(270)
        self.turtle.forward(distance)

    def draw_dots_x(self):
        for _ in range(self.n_dots_x):
            self.draw_dot()
            self.move("e", self.distance)

    def move_back_to_x_start(self):
        for _ in range(self.n_dots_x):
            self.move("w", self.distance)

    def hirst_painting(self):
        for _ in range(self.n_dots_y):
            self.draw_dots_x()
            self.move_back_to_x_start()
            self.move("n", self.distance)
        self.screen.exitonclick()


t.colormode(255)
painter = Painter(n_dots_x=10, n_dots_y=10, dot_diameter=20, spacing=50)
painter.turtle.speed(0)
painter.hirst_painting()
