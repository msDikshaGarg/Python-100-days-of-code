# Import relevant libraries
from turtle import Turtle
import random

# Making the Ball class
class Ball(Turtle):

    # Initializing the ball
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#9932CC")
        self.y_val = random.randint(5,10)
        self.x_val = random.randint(5,10)
        self.ball_speed = 0.1
        
    # Moving the ball on the screen
    def move(self):
        x = self.xcor() + self.x_val
        y = self.ycor() + self.y_val
        self.goto(x,y)

    # Bouncing the ball if it hits the top or bottom edge of screen
    def bounce_y(self):
        self.y_val = - self.y_val

    # Changing the ball speed 
    def random_speed(self):
        self.ball_speed *= 0.9

    # Bouncing the ball if a players hits the ball and increasing the ball speed slightly
    def bounce_x(self):
        self.x_val = - self.x_val
        self.random_speed()

    # Resetting the ball to its original position and speed if a player misses
    def ball_reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()

        