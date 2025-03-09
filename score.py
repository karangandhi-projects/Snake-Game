from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.points = 0
        with open("data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.points} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.points = 0
        self.update_score()

    def increase_score(self):
        self.points+=1
        self.update_score()