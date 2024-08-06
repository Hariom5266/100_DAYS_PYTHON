# 🍵 , Hanji Kaise ho aap sabhi this is 19th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== Understanding Turtle Coordinate System  ==================== #

import random
from turtle import Turtle,Screen

is_race_on=False

screen=Screen()

screen.setup(width=500,height=400)
users_bat=screen.textinput(title="Make your bet",prompt="Which turtle will win the race()? Enter a color: ")
# print(users_bat)
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    
if users_bat:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==users_bat:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
            
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()





