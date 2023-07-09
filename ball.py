from turtle import Turtle
from random import choice
from constants import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        # self.shapesize(2)
        self.fillcolor('blue')
        self.penup()
        self.setheading(choice(HEADING))

    def move(self):
        self.forward(20)

    def bounce_wall(self):
        cur_heading = self.heading()
        self.setheading(360 - cur_heading)

    def bounce_paddle(self):
        cur_heading = self.heading()
        self.setheading(180 - cur_heading)
