# 🍵 , Hanji Kaise ho aap sabhi this is 18th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# Strugle is Good

# ====================== Turtle Graphics,Tuples and importing Modules ====================== #

# Understanding Turtle Module

# it use for draw graphic on screen

# from turtle import Turtle,Screen
import turtle as t
import random

# timmy_the_turtle=Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# screen=Screen()
# screen.exitonclick()

# ====================== Draw Square ====================== #

timmy_the_turtle=t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for _ in range(4):
    # timmy_the_turtle.forward(100)
    # timmy_the_turtle.right(90)
    

# ====================== Draw Dashed Line ====================== #
# for _ in range(50):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
    

# ====================== Draw triangle,square,pentagon,hexgon,heptagon,octagon,nonagon,decagon ====================== #

# num_sides=5

# colors=["medium aqumarine","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle=360/num_sides
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
    
# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)
    
# trinket for turtle color

# # ====================== Generate Random Walk ====================== #

# colors=["DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# direction=[0,90,180,270]
# timmy_the_turtle.pensize(15)
# # timmy_the_turtle.speed(10)
# timmy_the_turtle.speed("fastest")

# for _ in range(500):
#     timmy_the_turtle.color(random.choice(colors))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))
    
# ====================== Tuples ==============C======== #

# # Tuples => it is datatype in python it has round bracket and seperated by comma
# # list() => for convert tuple to list

# tim=t.Turtle()
# t.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color=(r,g,b)
#     return random_color
    
# direction=[0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# ====================== Make a Spirograph ====================== #

tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):

    for _ in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
        tim.circle(100)
    
draw_spirograph(50)
    
# print(tim.heading())

# ====================== Import module and work with elise ====================== #

# Basic import
# import module_name
# from module import class/properties
# from turtle import * => import all thing => it is not best practice if use module more than three time then see on it

# Alasing module
# import turtle as t => here t is alias of module

# instaling modules
# import heroes
# print(heroes.gen()) # Generate random hero names

# use virtual environment for every project so we can make seperate project on python 3.12 and python 2




screen=t.Screen()
screen.exitonclick()


