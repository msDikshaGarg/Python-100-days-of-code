# importing the relevant classes
from turtle import Turtle, Screen

# Making our turtle object and coloring it shades of purple
voldetort = Turtle()
voldetort.shape("turtle")
voldetort.color("#9932CC", "#DDA0DD")
voldetort.pencolor("#9932CC")
voldetort.pensize(5)

# Making a square 
for i in range(0,4):
    voldetort.forward(200)
    voldetort.right(90)

# Screen controls
screen = Screen()
screen.exitonclick()