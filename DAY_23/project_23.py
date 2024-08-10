# 🍵 , Hanji Kaise ho aap sabhi this is 23th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Scoreboard
import time

# Setup the variable and object of game

screen=Screen()
is_game_on=True

# Setup the screen 

screen.title("Turtle Crossing")
screen.setup(width=600,height=600)
screen.tracer(0)

# Setup turtle 
player=Player()
car_manager=CarManager()
score=Scoreboard()

# player.shape("turtle")
# turtle.penup()
# turtle.goto(0,-280)

screen.listen()
screen.onkey(player.go_up,"Up")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    
    # Create and move the cars
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collison with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            is_game_on=False
            score.game_over()
            
    # Detect when turtle reaches the other side
    if player.ycor()>280:
        player.goto_start()
        car_manager.increase_speed()
        score.level_up()
        

screen.exitonclick()