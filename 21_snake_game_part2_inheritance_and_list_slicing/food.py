import random as r
from turtle import Turtle

import helpers as h


class Food(Turtle):
    def __init__(self, settings: object):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#80ed99")
        self.left(45)
        self.penup()
        self.SETTINGS = settings

    def get_random_cor(self):
        SCREEN_SIZE = self.SETTINGS.screen_size
        SEGMENT_LENGTH = self.SETTINGS.segment_length
        OFFSET = 3 * SEGMENT_LENGTH
        safe_area = int((SCREEN_SIZE / 2) - OFFSET)
        return (
            r.randrange(-safe_area, safe_area + 1, SEGMENT_LENGTH),
            r.randrange(-safe_area, safe_area + 1, SEGMENT_LENGTH),
        )

    def validate_food_placement(self, snake_segments: list):
        segments_cor = []
        for s in snake_segments:
            segments_cor.append(h.round_cor(s.segment.pos()))
        new_food_cor = segments_cor[0]
        while new_food_cor in segments_cor:
            new_food_cor = self.get_random_cor()
        return new_food_cor

    def spawn_food(self, snake_segments: list):
        self.goto(self.validate_food_placement(snake_segments))
