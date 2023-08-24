from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 14, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score=0
        self.l_score =0
        

    def update_scoreboard (self):
        self.goto(-100, 200)
        self.write(self.l_score, move="False", align=ALIGN, font=FONT)
        self.goto(100,200)
        self.write(self.r_score, move="False", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()
    

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move="False", align=ALIGN, font=FONT)
