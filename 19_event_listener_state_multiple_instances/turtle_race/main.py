import random as r
import turtle as t
from dataclasses import dataclass


@dataclass
class Racer:
    turtle: t.Turtle = None
    color: str = ""
    is_finish: bool = False


def personalize_racer(
    obj_turtle: t.Turtle, color: str, x_coord: float, y_coord: float
):
    obj_turtle.penup()
    obj_turtle.color(color)
    obj_turtle.goto(x_coord, y_coord)
    obj_turtle.showturtle()


def ordinal(index: int):
    n = index + 1
    return f"{n}{'st' if n == 1 else 
                 'nd' if n == 2 else 
                 'rd' if n == 3 else 'th'}"


# Setup canvas
screen = t.Screen()
width = 600
height = 300
t.setup(width, height)

# Setup racers
racers = []
colors = ["red", "blue", "green", "orange", "brown", "pink"]
num_racers = len(colors)

# Setup track
margin = 100
track_width = width - margin
track_height = height - margin

# Setup start line, finish line, and determine gap-y-axis between racer
start_line = -track_width / 2
finish_line = -start_line
bottom_y = -track_height / 2
gap_y = track_height / (num_racers - 1)

# Create and place racer on starting line
for i in range(num_racers):
    x = start_line
    y = bottom_y + (i * gap_y)
    racer = Racer()
    racer.color = colors[i]
    racer.turtle = t.Turtle(shape="turtle", visible=False)
    personalize_racer(racer.turtle, racer.color, x, y)
    racers.append(racer)

# User input (predict the winner) and validation
user_racer = None
while user_racer not in colors:
    user_racer = t.textinput(
        "Choose your champion!", "Who will win the race? Enter a color:"
    )
    if user_racer is None:
        continue
    else:
        user_racer = user_racer.strip().lower()

# Race
racer_at_finish_line = []
while not all([racer.is_finish for racer in racers]):
    for racer in racers:
        if racer.turtle.xcor() >= finish_line and not racer.is_finish:
            racer.is_finish = True
            racer_at_finish_line.append(racer)
            continue
        if racer.turtle.xcor() < finish_line and not racer.is_finish:
            racer.turtle.fd(r.randint(0, 15))

# Post race
winner = racer_at_finish_line[0].color
user_placing = ""
print("\nRace result:")
for i, racer in enumerate(racer_at_finish_line):
    if user_racer == racer.color:
        user_placing = ordinal(i)
    print(f"{ordinal(i)}: {racer.color.capitalize()}")

if user_racer == winner:
    print("\nCongratulation!\nYour champion Win 1st place!")
else:
    print(f"\nToo bad.\nYour champion is at {user_placing} place.")
