from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MAX_SCORE = 15

#Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#Disable screen tracing by default so we can use the screen.update() method to tell the program when to draw
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

#Enable the Screen listen function to listen for keystrokes.
#Bind the arrow keys to the respective direction method in the paddle object
screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with top or bottom of the screen (wall) and bounce the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle and bounce the ball
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 60) or (ball.xcor() < -320 and ball.distance(left_paddle) < 60):
        print("made contact with paddle")
        ball.bounce_x()

    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()

    #Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()

    if scoreboard.right_score >= MAX_SCORE or scoreboard.left_score >= MAX_SCORE:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()