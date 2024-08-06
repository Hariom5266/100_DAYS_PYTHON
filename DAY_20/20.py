# 🍵 , Hanji Kaise ho aap sabhi this is 20th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# from turtle import Turtle,Screen
# import time
# from snake import Snake

# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snack Game")
# screen.tracer(0)

# snake=Snake()

# ==================== Create body of Snacke ==================== #

# starting_position=[(0,0),(-20,0),(-40,0)]

# segments=[]

# for position in starting_position:
#     new_segment=Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
    

# ==================== Move the Snacke ==================== #

# game_is_on=True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
    
#     for seg_num in range(len(segments)-1,0,-1):
#         new_x=segments[seg_num-1].xcor()
#         new_y=segments[seg_num-1].ycor()
#         segments[seg_num].goto(new_x,new_y)
#     # segments[0].forward(20)
    # segments[0].left(90)
        

# ==================== Create a snake class and make it oop ==================== #
# it is in snake.py

from turtle import Turtle,Screen
from snake import Snake
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()




screen.exitonclick()

