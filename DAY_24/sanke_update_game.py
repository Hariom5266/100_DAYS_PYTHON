# 🍵 , Hanji Kaise ho aap sabhi this is 24th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()

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
    
    # Detect collision with food.
    
    # if snake.head.distance(food)<15:
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collison with wall.
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        
    # Detect collison with tail.
    # If head collison with any segment in the tail:
    # trigger game_over
    
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()


screen.exitonclick()


