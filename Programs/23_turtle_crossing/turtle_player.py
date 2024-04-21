# Import relevant libraries
from turtle import Turtle

# Paddle class
class Voldetort(Turtle):

    # Initializing the turtle
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#DDA0DD")
        self.penup()
        self.setposition(0, -280)
        self.setheading(90)

    # function to move the turtle up
    def up(self):
        self.forward(20)

    # function to reset the turtle position
    def reset(self):
        self.setposition(0, -280)