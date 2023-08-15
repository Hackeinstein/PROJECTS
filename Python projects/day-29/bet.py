from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False
color = ['red', 'blue', 'green', 'pink', 'orange', 'yellow']
yindex = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for tindex in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[tindex])
    new_turtle.goto(x=-230, y=yindex[tindex])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="result", prompt=f"You've won! The {winning_color} turtle is the winner! ")
            else:
                screen.textinput(title="result", prompt=f"You've lost! The {winning_color} turtle is the winner! ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
