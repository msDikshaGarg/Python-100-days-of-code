# Importing turtle 
from turtle import Turtle, Screen

# Creating objects
voldetort = Turtle()
screen = Screen()

program = True

# Shades of purple
voldetort.shape("turtle")
voldetort.color("#9932CC", "#DDA0DD")
voldetort.pencolor("#9932CC")
voldetort.pensize(2)

# Defining functions for forward, backward, rotation and clearing the screen
def move_forward():
    voldetort.forward(10)

def move_backward():
    voldetort.back(10)

def rotate_clockwise():
    voldetort.right(10)

def rotate_anticlockwise():
    voldetort.left(10)

def clear():
    voldetort.clear()
    voldetort.up()
    voldetort.home()
    voldetort.down()

# While the program runs
while program:
    # Screen listens 
    screen.listen()
    # Checks which key is pressed and calls the appropriate function
    screen.onkey(key="Up", fun=move_forward)
    screen.onkey(key="Down", fun=move_backward)
    screen.onkey(key="Right", fun=rotate_clockwise)
    screen.onkey(key="Left", fun=rotate_anticlockwise)
    screen.onkey(key="c", fun=clear)

    # When screen is clicked the program stops and the while loop ends
    screen.exitonclick()
    program = False