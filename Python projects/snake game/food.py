from turtle import Turtle
import random

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        rx=random.randint(-280,280)
        ry=random.randint(-280,280)
        self.refresh()

    def refresh (self):
        rx=random.randint(-280,280)
        ry=random.randint(-280,280)
        self.goto(rx,ry)