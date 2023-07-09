from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
from constants import *


def game_over(players, ball):
    ttl = Turtle()
    ttl.pencolor('white')
    if ball.xcor() >= WIDTH/2:
        ttl.write(f'Game over!    {players[0]} wins.', True,
                  'center', ('Arial', 20, 'bold'))
        return True
    elif ball.xcor() <= -WIDTH/2:
        ttl.write(f'Game over!    {players[1]} wins.', True,
                  'center', ('Arial', 20, 'bold'))
        return True
    return False


def hit_paddle(paddle, ball):
    distances = [segment.distance(ball) for segment in paddle.segments]
    return min(distances) <= 20


def game_setup(arena):
    player1 = arena.textinput(prompt= 'Enter name of first player',
                              title = 'Game setup')
    player2 = arena.textinput(prompt='Enter name of second player',
                              title='Game setup')

    return player1, player2


def dotted_line():
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.pencolor('white')
    tim.pensize(10)
    tim.goto(0, HEIGHT/2)
    tim.right(90)
    while tim.ycor() > -HEIGHT/2:
        tim.pendown()
        tim.forward(20)
        tim.penup()
        tim.forward(20)


def create_arena(arena):
    arena.title('Pong')
    arena.bgcolor('black')
    arena.setup(width=WIDTH, height=HEIGHT)
    dotted_line()
    arena.update()


def main():

    #Game setup
    arena = Screen()
    arena.tracer(0)

    create_arena(arena)
    ball = Ball()
    left_paddle = Paddle(-WIDTH/2 + 20)
    right_paddle = Paddle(WIDTH / 2 - 20)

    player1, player2 = game_setup(arena)
    score = Scoreboard([player1, player2])
    difficulty = arena.numinput(prompt='Enter difficulty level (1 - 5): ',
                                title='Choose difficulty')

    arena.update()
    arena.listen()

    while not game_over([player1, player2], ball):
        ball.move()
        arena.onkey(right_paddle.move_up, 'Up')
        arena.onkey(right_paddle.move_down, 'Down')
        arena.onkey(left_paddle.move_up, 'w')
        arena.onkey(left_paddle.move_down, 's')
        time.sleep(0.01 * (6 - difficulty))
        if abs(ball.ycor()) >= HEIGHT/2 - 20:
            ball.bounce_wall()
        if hit_paddle(left_paddle, ball):
            score.update(0)
            ball.bounce_paddle()
        if hit_paddle(right_paddle, ball):
            score.update(1)
            ball.bounce_paddle()
        arena.update()
    arena.exitonclick()


if __name__ == '__main__':
    main()
