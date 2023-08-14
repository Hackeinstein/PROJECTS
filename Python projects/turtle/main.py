from turtle import Turtle, Screen
import random

timmy  = Turtle()

#dotted lines

# for i in range (15):
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.pendown()
# timmy.forward(20)

# shapes and sides
# def draw (num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)

# for sides in range (3,100):
#     draw(sides)

#random walk
# moves=["right","left"]
# colours=['red',"blue","yellow","green"]
# timmy.speed(10)
# timmy.pensize(10)

# for i in range (1000):
#     move=random.choice(moves)
#     timmy.pencolor(random.choice(colours))
#     if move=="right":
#         timmy.right(90)
#         timmy.forward(20)
#     elif move=="left":
#         timmy.left(90)
#         timmy.forward(20)



timmy.circle(radius=100)
timmy.circle(radius=100, steps=5)














screen = Screen()
screen.mainloop()