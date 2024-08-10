from turtle import Turtle

FONT=("Coursier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.penup()
        self.color("black")
        self.goto(-260,260)
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)
        
    def level_up(self):
        self.level+=1
        self.write_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER...!😒",align="center",font=FONT)