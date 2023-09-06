import turtle as t
import random

tim = t.Turtle()
#tim.shape("turtle")
#tim.color("red")

#Challenge 1 - Draw a 100px Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

#Challenge2  - Draw a dashed line
# for _ in range(15):
    # one method is to change color between black and white
    # tim.forward(10)
    # tim.color("white")
    # tim.forward(10)
    # tim.color("black")

    # another method is to use the pendown() and penup() methods in the Turtle object
    # tim.forward(10)
    # tim.penup()
    # tim.forward(10)
    # tim.pendown()

#Challenge 3 - Draw different shapes with different colors
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# For each angle, use 360 / (num sides)

colors = ["red", "orange", "gold", "green", "blue", "indigo", "dark violet", "violet"]

# def draw_shape(num_sides):
#     angle = int(360 / num_sides)
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for num_sides in range(3,11):
#     tim.color(colors[num_sides - 3])
#     draw_shape(num_sides)


# Challenge 4 - Draw a random walk.  Random direction, random distance, random colors
# tim.pensize(10) 
# turn_direction = [0, 90, 180, 270]
# trip_length = random.randint(50,500)
# #print(trip_length)
# tim.speed(10)
# for _ in range(trip_length):
#     distance = random.randint(1,30)
#     #print(distance)
#     color = random.choice(colors)
#     #print(color)
#     direction = random.choice(turn_direction)
#     #print(direction)
#     tim.color(color)
#     tim.setheading(direction)
#     tim.forward(distance)

#Challenge 4 - refactored Generate random RGB colors
# Create a function to generate and return a tuple of random numbers between 0 and 255
# Use that tuple in the tim.color().  Also set the colormode (from turtle module) to 255
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
    
# tim.pensize(10) 
# turn_direction = [0, 90, 180, 270]
# trip_length = random.randint(50,500)
# #print(trip_length)
# tim.speed(10)
# for _ in range(trip_length):
#     distance = random.randint(1,30)
#     #print(distance)
#     color = random_color()
#     #print(color)
#     direction = random.choice(turn_direction)
#     #print(direction)
#     tim.color(color)
#     tim.setheading(direction)
#     tim.forward(distance)

# Challenge 5 - Draw a spirograph. - Draw a circle, change the angle and color, repeat
tim.speed("fastest")
for heading in range (0,360,5):
    color = random_color()
    tim.color(color)
    tim.setheading(heading)
    tim.circle(100)


screen = t.Screen()
screen.exitonclick()