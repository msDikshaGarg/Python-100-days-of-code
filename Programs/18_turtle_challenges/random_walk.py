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
voldetort.pensize(10)

directions = [0, 90, 180, 270]

# Sides max is 10 since we are going to decagon
for i in range(100):
    # Picking random RGB values using the random module
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    # Setting the pencolor to the randomly chosen color using RBG values 
    voldetort.pencolor((R, G, B))
    # Walking
    voldetort.forward(20)
    voldetort.setheading(random.choice(directions))

screen.exitonclick()
