from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0 
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier",80,"normal"))
         
    def l_point(self):
        self.l_score+=1
        self.update()
    
    def r_point(self):
        self.r_score +=1
        self.update()
    
    def winner(self):
        self.goto(0,0)
        if self.l_score > self.r_score:
            self.write("Left side Won", align="center", font=("Courier",40,"normal"))
        else:
            self.write("Right side Won", align="center", font=("Courier",40,"normal"))
