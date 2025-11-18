import time
from dataclasses import dataclass
from turtle import Screen, Turtle


@dataclass
class Segment:
    snake: Turtle = None
    cor: tuple = None
    prev_cor: tuple = None


def head_direction(head: Segment, direction: str):
    current = head.snake.heading()
    new = {"e": 0, "n": 90, "w": 180, "s": 270}[direction]
    if abs(new - current) != 180:
        head.snake.seth(new)


def is_hit_wall(wall: int, obj_body: Segment):
    xcor, ycor = obj_body.cor
    if abs(xcor) >= wall or abs(ycor) >= wall:
        return True
    return False


def logic_snake_movement(segments: list, distance: int):
    for i, segment in enumerate(segments):
        segment.prev_cor = segment.snake.pos()
        if i == 0:
            segment.snake.fd(distance)
        else:
            segment.snake.goto(segments[i - 1].prev_cor)
        segment.cor = segment.snake.pos()


# Setup Screen
screen = Screen()
game_field = 600
screen.setup(width=game_field, height=game_field)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Snake settings
segment_length = 20
init_segment_counts = 3
game_mov_speed = 0.1  # in seconds

# Init snake
segments = []
for i in range(init_segment_counts):
    xcor = i * (segment_length) * -1
    ycor = 0
    new_segment = Segment()
    new_segment.snake = Turtle(shape="square")
    new_segment.cor = (xcor, ycor)
    new_segment.snake.penup()
    new_segment.snake.color("white")
    new_segment.snake.goto(xcor, ycor)
    segments.append(new_segment)

head = segments[0]

# Keybinding - snake movement
screen.listen()
screen.onkey(key="Right", fun=lambda: head_direction(head, "e"))
screen.onkey(key="Up", fun=lambda: head_direction(head, "n"))
screen.onkey(key="Left", fun=lambda: head_direction(head, "w"))
screen.onkey(key="Down", fun=lambda: head_direction(head, "s"))

# Game play
is_game_over = False
wall = (game_field / 2) - segment_length
while not is_game_over:
    time.sleep(game_mov_speed)
    logic_snake_movement(segments, segment_length)
    # Wall collision
    if is_hit_wall(wall, head):
        is_game_over = True
    screen.update()

# TODO: Body collision
# TODO: Generate food + random placing
# (need body detection, not placing food on current body)
# TODO: Increase body count after eat food
# TODO: Display score
# TODO: Restart Mechanics
# TODO: Persistent personal high-score
# TODO: Level mechanics
# (snake move faster after eat certain amount of food)
# TODO: Refactor


screen.exitonclick()

# BUG: sometimes, snake can do u-turn when2 keys are pressed at same time
