# from colorgram import extract
#
# colors = extract('image.jpg', 10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
from random import choice

color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# tim.pendown()
# print(tim.xcor())
tim.setposition(-212, -212)
for row in range(10):
    for col in range(10):
        tim.pendown()
        # tim.color(choice(color_list))
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)
    # tim.left(90)
    # tim.forward(20)
    tim.setposition(-212, (row+1)*50-212)



screen = Screen()
# screen.screensize(2000, 2000)
screen.exitonclick()
