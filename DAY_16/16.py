# 🍵 , Hanji Kaise ho aap sabhi this is 16th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== Why need of OOP ====================== #

# Procedual Programming -- Fortan it use this type of programming, it is confugion and in it we make fnc for any funcnality

# if we make safe driveing car software then i want to use its module in dron system then i can use it by oop

# one man resturant -- it is complex like if procedual programming

# ====================== How to use Calsses and obj ====================== #

# use of it bcz it trying to implement real world models
# create a virtual resturant and in it waiter what is has and what  is does
# has means attributes it is variable which associated with obj
# what is does means fnc associated with obj that define it work or funcalities
# obj means just the way of combining piece of data and some functionality alogether in the same thing.
# but we have many obj like we have many waiter in our virtual restro so we need to generate multi data and they have some piece of data that is same it called blueprint and define the blueprint or way of define bluprint in programming called class.

# ====================== Constructing Object ====================== #

# car = CarBluePrint() -- use piscal case here car is obj and CarBluePrint is blueprint or class.
# Turtle Graphics

# ====================== Create Obj ====================== #

# # use documentation of turtle graphic for this library

# # import turtle   
# from turtle import Turtle,Screen

# # timmy=turtle.Turtle()
# # print(timmy) -- it give it address
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red") # it change color of turtle
# timmy.forward(100)
# my_screen=Screen()
# # here my_screen is object and canvheight is attribute which assosicated with my_screen
# print(my_screen.canvheight)
# my_screen.exitonclick() # process finish when we click on screen

# ====================== Python Packages ====================== #

# packeges is bunch of code that written by devloper for achieve a goal

# make table is very difficlt for it use packages on pypi.org

# PyPi - python package index where all packages are included

# for table use prettytable

# import prettytable
from prettytable import PrettyTable
table=PrettyTable()
# for add columns is add_colum("field name",list of data)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charamander"])
table.add_column("Type",["Electric","Water","Fire"])

# Change object attributes
table.align='r'

print(table)
