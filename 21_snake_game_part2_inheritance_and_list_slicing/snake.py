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
        self.boot()

    def add_segment(self, num_segment: int, is_init: bool):
        for i in range(num_segment):
            new = Segment()
            new.segment = Turtle(shape="square")
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

    def boot(self):
        self.add_segment(self.segment_count, True)
        self.head = self.segments[0]

    def move(self):
        for i, s in enumerate(self.segments):
            s.prev_cor = s.segment.pos()
            if i == 0:
                s.segment.fd(self.segment_length)
            else:
                s.segment.goto(self.segments[i - 1].prev_cor)
            s.cor = s.segment.pos()
