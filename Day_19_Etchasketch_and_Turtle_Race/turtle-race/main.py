from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title ="Make your bet", prompt="Which turtle will win the race?  \nEnter a color (red, orange, yellow, green, blue, purple): ")
while user_bet not in colors:
    user_bet = screen.textinput(title ="Make your bet", prompt="Invalid color.  Which turtle will win the race?  \n Enter a color (red, orange, yellow, green, blue, purple): ")
#print(user_bet)

y_start = [-75, -45, -15, 15, 45, 75]
all_turtles = []

#Create 7 turtles, one for each color and assign to a list so they can be referenced in the race   
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_start[turtle_index])  
    all_turtles.append(new_turtle)

#Set the is_race_on boolean to True so the race will loop
if user_bet:
    is_race_on = True

#Keep looping until a turtle finishes. The x coordinate is the right side of the screen minus half the turtle size (20)
#For each turtle in each iteration, generate a random distance that turtle will move.
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!  The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!  The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()