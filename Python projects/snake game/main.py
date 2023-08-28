from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


screen.update()
game_Active = True

while game_Active:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # detect collision with tail
    for seg in snake.full_seg[1:]:
        if snake.head.distance(seg)<10:
           scoreboard.reset() 



screen.exitonclick()
