# 🍵 , Hanji Kaise ho aap sabhi this is 18th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== The Hirst Painting Project ====================== #

# ====================== Do this for generate Color from images ====================== #

# import colorgram

# # Provide the absolute path to the image
# image_path = 'C:\\Users\\Lenovo\\Desktop\\01_HC_JOSHI\\Work\\100_DAYS_OF_PYTHON\\DAY_18\\hirst-painting-start\\image.jpg'

# # Extract colors from the image
# colors = colorgram.extract(image_path, 38)
# here 38 is no of color i want to extreted from the image

# # List to hold the RGB values
# rgb_colors = []

# # Iterate over the extracted colors
# for color in colors:
#     # Access the RGB property
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# # Print the list of RGB colors
# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()




