# 🍵 , Hanji Kaise ho aap sabhi this is 19th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== More Turtle Graphics, Higher Order Fnc, State and Multiple Instance,Evnet Listeners ==================== #

# ==================== Higher Order Fnc and Event Listener ==================== #

# from turtle import Turtle,Screen
# tim=Turtle()
# screen=Screen()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space",fun=move_forwards) # fnc as a input 
# screen.exitonclick()

# higher order fnc means it is fnc that can work with another fnc which take fnc as a input and work with it

# ==================== Make a Sketch App ==================== #

from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
    
def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")



screen.exitonclick()

# ==================== Object State ==================== #



