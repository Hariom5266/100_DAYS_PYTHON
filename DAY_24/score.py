from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",34,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("C:/Users/Lenovo/Desktop/01_HC_JOSHI/Work/100_DAYS_OF_PYTHON/DAY_24/high_score.txt") as data:
            self.high_score=int(data.read())
            
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALIGNMENT,font=FONT)
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            
            with open("C:/Users/Lenovo/Desktop/01_HC_JOSHI/Work/100_DAYS_OF_PYTHON/DAY_24/high_score.txt",mode='w') as data:
                data.write(f"{self.high_score}")
                
        self.score=0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
  