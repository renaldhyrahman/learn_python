from dataclasses import dataclass
from turtle import Turtle


@dataclass
class Segment:
    segment: Turtle = None
    cor: tuple = None
    prev_cor: tuple = None


class Snake:
    def __init__(self, settings: object):
        self.segment_length = settings.segment_length
        self.segment_count = settings.segment_count
        self.segments = []
        self.snake_create()

    def segment_add(self, segment_num: int, is_init: bool = False):
        for i in range(segment_num):
            new = Segment()
            new.segment = Turtle(shape="square")
            new.segment.shapesize(stretch_wid=0.9, stretch_len=0.9)
            new.segment.penup()
            new.segment.color("white")
            if is_init:
                xcor = i * (self.segment_length) * -1
                ycor = 0
            else:
                last = self.segments[-1]
                xcor, ycor = last.cor
            new.cor = (xcor, ycor)
            new.segment.goto(xcor, ycor)
            self.segments.append(new)

    def snake_create(self):
        self.segment_add(self.segment_count, True)
        self.head = self.segments[0]

    def move(self):
        for i, s in enumerate(self.segments):
            s.prev_cor = s.segment.pos()
            if i == 0:
                s.segment.fd(self.segment_length)
            else:
                s.segment.goto(self.segments[i - 1].prev_cor)
            new_x = round(s.segment.pos()[0], 2)
            new_y = round(s.segment.pos()[1], 2)
            s.cor = (new_x, new_y)

    def hide(self):
        for s in self.segments:
            s.segment.ht()

    def reset(self):
        self.hide()
        self.head = None
        self.segments = []
        self.snake_create()
