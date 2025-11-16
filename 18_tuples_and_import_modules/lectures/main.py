import random as r
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

# CHALLENGE #1
# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# CHALLENGE #2
# Draw a dash #1
# for _ in range(15):
#     tim.forward(10)
#     tim.teleport(tim.pos()[0] + 10)
# print(tim.pos())
# Draw a dash #2 (Angela solution)
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# CHALLENGE #3
# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# t.colormode(255)
# def draw_shapes(num_sides: int, length: int, obj_turtle: t.Turtle):
#     angle = 360 / num_sides
#     obj_turtle.pencolor(
#         (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
#     )
#     for _ in range(num_sides):
#         obj_turtle.forward(length)
#         obj_turtle.right(angle)
# for number in range(3, 11):
#     draw_shapes(number, 100, tim)


# CHALLENGE #4
# Draw a random walk
# t.colormode(255)
# def challenge_4(
#     pen_size: int,
#     speed: int,
#     distance: int,
#     n_times: int,
#     obj_turtle: t.Turtle,
# ):
#     obj_turtle.pensize(pen_size)
#     obj_turtle.speed(speed)
#     for _ in range(n_times):
#         random_color_tuple = (
#             r.randint(0, 255),
#             r.randint(0, 255),
#             r.randint(0, 255),
#         )
#         obj_turtle.pencolor(random_color_tuple)
#         obj_turtle.setheading(r.choice([0, 90, 180, 270]))
#         obj_turtle.forward(distance)
# challenge_4(pen_size=15, speed=0, distance=30, n_times=300, obj_turtle=tim)

# CHALLENGE #5
# Draw a Spirograph #1
t.colormode(255)


def draw_spirograph(
    n_times: int,
    distance: int,
    speed: int,
    is_random_color: bool,
    obj_turtle: t.Turtle,
):
    angle = 360 / n_times
    obj_turtle.speed(speed)
    for _ in range(n_times):
        obj_turtle.left(angle)
        if is_random_color:
            obj_turtle.pencolor(
                (
                    r.randint(0, 255),
                    r.randint(0, 255),
                    r.randint(0, 255),
                )
            )
        obj_turtle.circle(distance)


draw_spirograph(100, 100, 0, True, tim)


# Draw a Spirograph #2 (Angela solution)
# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# tim.speed("fastest")

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
