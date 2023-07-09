from turtle import Turtle
from constants import *


class Paddle():
    def __init__(self, x_loc):
        self.segments = []

        for i in range(7):
            self.extend((x_loc, -60 + 20 * i))

    def extend(self, loc):
        ttl = Turtle()
        ttl.shape('square')
        ttl.fillcolor('white')
        ttl.penup()
        ttl.goto(loc)
        self.segments.append(ttl)

    def move_up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(20)

    def move_down(self):
        for segment in self.segments:
            segment.setheading(-90)
            segment.forward(20)