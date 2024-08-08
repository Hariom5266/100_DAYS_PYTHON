# 🍵 , Hanji Kaise ho aap sabhi this is 22th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score()

# paddle=Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() 
    ball.move()
    
    # Detect collison with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    
    # Detect when paddle is missing
    
    # if right side paddle miss the ball.
    
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        
    # if left side paddle miss the ball.

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        
    




screen.exitonclick()