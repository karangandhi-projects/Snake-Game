import random
from turtle import Turtle
MAX = 260
MIN = -260

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(MIN,MAX)
        random_y = random.randint(MIN,MAX)
        self.goto(random_x,random_y)