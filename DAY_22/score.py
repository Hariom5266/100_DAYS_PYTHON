from turtle import Turtle

CENTER="center"
FONT=("Coursier",88,"normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=CENTER,font=FONT)    
        self.goto(100,200)
        self.write(self.r_score,align=CENTER,font=FONT)
    
    def l_point(self):
        self.l_score+=1
        self.update_score()
    
    def  r_point(self):
        self.r_score+=1
        self.update_score()