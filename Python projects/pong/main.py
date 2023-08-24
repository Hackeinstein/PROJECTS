from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
game_Active=True


paddle_1=Paddle(350)
paddle_2=Paddle(-350)
ball=Ball()
scoreboard =Scoreboard()



#controls
screen.listen()
screen.onkeypress(paddle_1.up, "Up")
screen.onkeypress(paddle_1.down,"Down")
screen.onkeypress(paddle_2.up, "w")
screen.onkeypress(paddle_2.down,"s")



while game_Active:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    # detect collison with right paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) <50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()