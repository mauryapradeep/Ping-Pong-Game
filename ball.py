from turtle import Turtle
# Balls
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.setposition(0,0)
        self.x_move = 10
        self.y_move =10
        self.ball_speed = 0.1


    def move(self):

        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move

        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()
