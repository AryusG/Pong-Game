# Features that need their own classes

# Screen / including the net
# Ball -> detect collision with wall and bounce -> detect collision with paddle
# Left/Right score -> detect when paddle misses

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title('Pong!')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)


r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() < 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_increase()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score_increase()

screen.exitonclick()