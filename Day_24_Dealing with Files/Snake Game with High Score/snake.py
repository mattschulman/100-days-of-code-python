from turtle import Turtle

#Constants definitions
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 17
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self):
        # To initialize, create an empty list to store the Turtle objects and then call the method to create the segments and
        # assign to the segments list.
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        #create a new Turtle object (segment) for each position in the STARTING_POSITIONS list. Pass in the position argument
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        #Create a square Turtle object, set the color, turn off the line drawing, 
        #send to the starting position, and then append the Turtle object to a list so it can be referenced later.
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())


    def move(self):
        #In order to move the snake, move the snake segments from the last to the first.
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Do not change direction if headed in opposite direction.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Do not change direction if headed in opposite direction.
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Do not change direction if headed in opposite direction.
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def right(self):
        # Do not change direction if headed in opposite direction.
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]