from turtle import Turtle
import random

RAND_Y=random.randint(-270,270)

class Paddle (Turtle):
    def __init__(self,side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=side,y=RAND_Y)

    def up (self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down (self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)