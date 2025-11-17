import turtle as t


def reset(obj_painter: t.Turtle):
    obj_painter.clear()
    obj_painter.penup()
    obj_painter.home()
    obj_painter.pendown()


painter = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkey(key="w", fun=lambda: painter.fd(10))
screen.onkey(key="s", fun=lambda: painter.bk(10))
screen.onkey(key="a", fun=lambda: painter.left(10))
screen.onkey(key="d", fun=lambda: painter.right(10))
screen.onkey(key="c", fun=lambda: reset(painter))

screen.exitonclick()
