from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.cords = [0, -20, -40]
        self.full_seg = []
        
        # create snakes
        for i in range(3):
            self.seg = Turtle("square")
            self.seg.color("white")
            self.seg.penup()
            self.seg.goto(x=self.cords[i], y=0)
            self.full_seg.append(self.seg)
        self.head=self.head

    def move(self):
        for seg in range(len(self.full_seg)-1, 0, -1):
            new_X = self.full_seg[seg-1].xcor()
            new_Y = self.full_seg[seg-1].ycor()
            self.full_seg[seg].goto(new_X, new_Y)
        self.head.forward(20)
    
    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right (self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left (self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)