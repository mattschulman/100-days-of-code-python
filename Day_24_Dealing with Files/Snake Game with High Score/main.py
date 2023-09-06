from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def game_over():
    global game_is_on 
    game_is_on =  False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
#Disable screen tracing by default so we can use the screen.update() method to tell the program when to draw
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Enable the Screen listen function to listen for keystrokes.
#Bind the arrow keys to the respective direction method in the snake object
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="q", fun=game_over)

game_is_on = True
while game_is_on:
    #Now that the starting segments are created, tell the program to draw. Update after each move
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food, move food to a new location, add a snake segmnent,  and update the scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall - tell the while loop to stop looping and write a game over message
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #Detect collision with any snake segment (except the head - use a slice to exclude index 0) and tell the while loop to 
    # stop looping and write a game over message
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()