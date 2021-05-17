# Features that need their own classes

# Screen / including the net
# Ball -> detect collision with wall and bounce -> detect collision with paddle
# Left/Right score -> detect when paddle misses

from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title('Pong!')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)


r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_on = True

while game_on:
    screen.update()


screen.exitonclick()