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
# increasing turtle speed
voldetort.speed('fastest')

def random_color():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    # Setting the pencolor to the randomly chosen color using RBG values 
    return voldetort.pencolor((R, G, B))

angle = 0

while angle < 361:
    random_color()
    # Starting with facing the angle as it changes
    voldetort.setheading(angle)
    # Making the circle
    voldetort.circle(100)
    # Increasing starting angle to turn the turtle starting angle by 5 degrees
    angle +=5

screen.exitonclick()
