# Import relevant libraries
from turtle import Turtle

# Paddle class
class Score(Turtle):

    # Initializing the turtle
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#DDA0DD")
        self.penup()
        self.setposition(-380, 260)
        self.curr_score = 0
        self.write(f"Score : {self.curr_score}", align = "left", font=("Arial", 24, 'normal'))

    def update_score(self):
        self.clear()
        self.curr_score += 1 
        self.write(f"Score : {self.curr_score}", align = "left", font=("Arial", 24, 'normal'))

    def game_over(self):
        self.setposition(-65, 0)
        self.write("Game Over", font = ('Arial', 24, 'normal'))
        self.goto(-65, -20)
        self.write(f"Your final score is {self.curr_score}.", font = ('Arial', 24, 'normal'))
