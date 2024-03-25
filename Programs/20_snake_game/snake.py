# Import relevant libraries
from turtle import Turtle

# Setting standard variables
STEPS = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

# Snake class
class Snake:
    
    # Initializing the snake
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.first = self.segments[0]
        self.first.shape("triangle")

    # Creating the first 3 segments of the snake to start with
    def create_snake(self):
        for i in range(0,3):
            new_seg = Turtle("square")
            new_seg.color("#DDA0DD")
            new_seg.penup()
            new_seg.setx(i*-20)
            self.segments.append(new_seg)

    # Adding a segment at the last position when the snake eats food
    def add_segment(self):
        new_seg = Turtle("square")
        new_seg.color("#DDA0DD")
        new_seg.penup()
        new_seg.setposition(self.segments[-1].position())
        self.segments.append(new_seg)

    # Moving the segments forwards together
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(STEPS)

    # Moving up when the player presses the up key
    def up(self):
        if self.first.heading() != DOWN:
            self.first.setheading(UP)

    # Moving down when the player presses the down key
    def down(self):
        if self.first.heading() != UP:
            self.first.setheading(DOWN)

    # Moving right when the player presses the right key
    def right(self):
        if self.first.heading() != LEFT:
            self.first.setheading(RIGHT)

    # Moving left when the player presses the left key
    def left(self):
        if self.first.heading() != RIGHT:
            self.first.setheading(LEFT)
