# importing the relevant classes
from turtle import Turtle, Screen

# Making our turtle object and coloring it shades of purple
voldetort = Turtle()
voldetort.shape("turtle")
voldetort.color("#9932CC", "#DDA0DD")
voldetort.pencolor("#9932CC")
voldetort.pensize(2)

# Making a dashed line 
for i in range(20):
    voldetort.forward(5)
    voldetort.up()
    voldetort.forward(5)
    voldetort.down()

# Screen controls
screen = Screen()
screen.exitonclick()