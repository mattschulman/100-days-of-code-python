# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,b,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Generate a 10 x 10 set of dots.  Dots are 20 in size and spaced by 50.

import turtle as t
import random

color_list = [(202, 110, 110), (149, 50, 50), (222, 136, 136), (53, 123, 123), (170, 41, 41), (138, 20, 20), 
               (134, 184, 184), (197, 73, 73), (47, 86, 86), (73, 35, 35), (145, 149, 149), (14, 70, 70), 
               (232, 165, 165), (160, 158, 158), (54, 50, 50), (101, 77, 77), (183, 171, 171), (36, 74, 74), 
               (19, 89, 89), (82, 129, 129), (147, 19, 19), (27, 102, 102), (12, 64, 64), (107, 153, 153), 
               (176, 208, 208), (168, 102, 102)]

dot = t.Turtle()
t.colormode(255)
dot.speed(0)
dot.shape("classic")
dot.penup()
dot.hideturtle()

def create_dot():
    fill_color = random.choice(color_list)
    dot.dot(20,fill_color)

for y in range (-225, 226, 50):
    for x in range (-225,226, 50):
        dot.goto(x,y)
        create_dot()

screen = t.Screen()
screen.exitonclick()