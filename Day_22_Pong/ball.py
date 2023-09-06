from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #self.setheading(45)
        #define the starting x and y coordinate adds for moving the ball
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse the y movement direction by flipping pos to neg or neg to pos
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the x movement direction by flipping pos to neg or neg to pos
        # Also increase the speed
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        #Reset the ball's position back to the center but flip the x-axis and reset the speed
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()