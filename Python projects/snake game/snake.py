from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.cords = [0, -20, -40]
        self.full_seg = []
        self.create_snake()
        
        # create snakes
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)
        self.head=self.full_seg[0]

    def add_segments (self,_position):
        self.seg = Turtle("square")
        self.seg.color("white")
        self.seg.penup()
        self.seg.goto(_position)
        self.full_seg.append(self.seg)
        


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
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def extend (self):
        self.add_segments(self.full_seg[-1].position())

    def reset (self):
        for segs in self.seg:
            segs.goto(1000,1000)
        self.seg.clear()
        self.create_snake()