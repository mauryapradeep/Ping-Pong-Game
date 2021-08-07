from turtle import Screen, Turtle
from paddle_movement import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height= 600, width= 800)
screen.title("pong: the famous arcade game")
screen.tracer(0)

l_paddle = Paddle((-370,0))
r_paddle = Paddle((370,0))
ball =  Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.go_up,"Up" )
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w" )
screen.onkey(l_paddle.go_down, "s")

time.sleep(0.1)
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()
# detect collision with with wall
    if ball.ycor() == 280 or ball.ycor() == -280 :
        ball.bounce_y()

# detect collision with  paddles
    if ball.xcor()>330 and ball.distance(r_paddle)<50 or ball.xcor()<-330 and ball.distance(l_paddle)<50 :
        ball.bounce_x()

# ditect right paddle misses
    if ball.xcor() > 380 :
        ball.reset()
        scoreboard.l_point()

# ditect left paddle misses
    if  ball.xcor()< -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
