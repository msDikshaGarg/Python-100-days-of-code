# importing the relevant classes
from turtle import Turtle, Screen
import random

# Screen controls
screen = Screen()
# Setting colormode to RGB 0-255
screen.colormode(255)

# Making our turtle object and coloring it shades of purple
voldetort = Turtle()
voldetort.shape("turtle")
voldetort.color("#9932CC", "#DDA0DD")
#voldetort.pencolor("#9932CC")
voldetort.pensize(2)

# Starting with 3 sides since first shape is triangle
sides = 3 

# Sides max is 10 since we are going to decagon
while sides <= 10:
    # Angle to turn is total (360) divided by number of sides in the shape 
    angle = 360 / sides
    # Picking random RGB values using the random module
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    # Setting the pencolor to the randomly chosen color using RBG values 
    voldetort.pencolor((R, G, B))
    # Making the shape
    for i in range(sides):
        voldetort.forward(50)
        voldetort.right(angle)
    # Increasing the number of sides by 1 to make the next shape
    sides +=1

screen.exitonclick()
