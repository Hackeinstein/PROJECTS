from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 14, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score =0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move=False, align=ALIGN, font=FONT)
        with open("data.txt") as data:
           self.high_score = int(data.read())

    def increase(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard (self):
        self.clear()
        self.write(f"Score: {self.score}",
                   move="False", align=ALIGN, font=FONT)
        

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move="False", align=ALIGN, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()