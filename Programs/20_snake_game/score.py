# Import relevant libraries
from turtle import Turtle

# Setting the standard font for the text
FONT = ('Arial', 24, 'normal')

# Score class to calculate scores and maintain game text
class Score(Turtle):

    # Initializing the turtle to write text and hide itself,also making a score variable
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#DDA0DD")
        self.score = 0
        self.score_update()

    # Update the score on the screen by clearing the previous text and writing the new score at the same place
    def score_update(self):
        self.clear()
        self.setposition(-40, 270)
        self.write(f"Score : {self.score}", font=FONT)

    # If the snake has a collision it prints game over
    def collision(self):
        self.setposition(-65, 0)
        self.write(";-; Game Over ;-;", font=FONT)