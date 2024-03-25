# Import relevant libraries
from turtle import Turtle

# Paddle class
class Paddle(Turtle):

    # Initializing the paddle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#DDA0DD")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(position)
    
    # Moving up when the player presses the up key
    def up(self):
        if self.ycor() < 180:  
            self.y = self.ycor() + 20
            self.sety(self.y)

    # Moving down when the player presses the down key
    def down(self):
        if self.ycor() > -180:
            self.y = self.ycor() - 20
            self.sety(self.y)

