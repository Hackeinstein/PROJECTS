from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 14, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",
                   move="False", align=ALIGN, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.write(f"Score: {self.score}",
                   move="False", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move="False", align=ALIGN, font=FONT)
