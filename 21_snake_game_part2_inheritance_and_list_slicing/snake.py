from dataclasses import dataclass
from turtle import Turtle

import helpers as h


@dataclass
class Segment:
    segment: Turtle = None
    prev_cor: tuple = None


class Snake:
    def __init__(self, settings: object):
        self.segment_length = settings.segment_length
        self.segment_count = settings.segment_count
        self.segments = []
        self.create()

    def segment_add(self, cor: tuple):
        new = Segment()
        new.segment = Turtle(shape="square")
        new.segment.shapesize(stretch_wid=0.9, stretch_len=0.9)
        new.segment.penup()
        new.segment.color("white")
        new.segment.goto(cor)
        self.segments.append(new)

    def create(self):
        for i in range(self.segment_count):
            xcor = i * (self.segment_length) * -1
            self.segment_add((xcor, 0))
        self.head = self.segments[0]

    def extend(self):
        self.segment_add(self.segments[-1].segment.pos())

    def move(self):
        for i, s in enumerate(self.segments):
            s.prev_cor = h.round_cor(s.segment.pos())
            if i == 0:
                s.segment.fd(self.segment_length)
            else:
                s.segment.goto(self.segments[i - 1].prev_cor)

    def hide(self):
        for s in self.segments:
            s.segment.ht()

    def reset(self):
        self.hide()
        self.segments = []
        self.create()
