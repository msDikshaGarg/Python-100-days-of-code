# Import relevant libraries
from turtle import Turtle
import random

# Making the Food class
class Food(Turtle):

    # Initializing the food shape and color 
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#9932CC")
        self.shapesize(0.5)
        self.new_pos()

    # Moving the food to a random new position 
    def new_pos(self):
        self.setposition((random.randint(-250,250), random.randint(-250,250)))
