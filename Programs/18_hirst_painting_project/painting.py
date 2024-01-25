from extract_color import rgb_colors
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
voldetort.speed('fast')

# Starting position
x = -250
y = -250
voldetort.up()
voldetort.setpos((x,y))

# Loop for 10 rows
for i in range(10):
    # Loop for 10 circles in a row
    for j in range (10):
        # Changing pen color
        voldetort.pencolor(random.choice(rgb_colors))
        # Making the dot
        voldetort.down()
        voldetort.dot(20)
        # Lifting the pen and moving forward
        voldetort.up()
        voldetort.forward(50)
    # Changing y coordinate to go up by 50 spaces
    y += 50
    # Setting new position to move up a row
    voldetort.setpos((x, y))
voldetort.hideturtle()

screen.exitonclick()

