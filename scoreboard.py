from turtle import Turtle
from constants import *


class Scoreboard(Turtle):
    def __init__(self, players):
        super().__init__()
        self.players = players
        self.score = [0, 0]
        for i in range(2):
            self.penup()
            self.pencolor('white')
            self.hideturtle()
            self.goto((-100 + 200 * i, HEIGHT/2 - 50))
            self.write(f'{self.players[i]} \n {self.score[i]}', True,
                       'center', ('Arial', 18, 'bold'))

    def update(self, idx):
        self.clear()
        self.score[idx] += 1
        for i in range(2):
            self.goto((-100 + 200 * i, HEIGHT / 2 - 50))
            self.write(f'{self.players[i]} \n {self.score[i]}', True,
                       'center', ('Arial', 18, 'bold'))
