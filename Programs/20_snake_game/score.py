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
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.score_update()

    # Update the score on the screen by clearing the previous text and writing the new score at the same place
    def score_update(self):
        self.clear()
        self.setposition(-150, 270)
        self.write(f"Score : {self.score}  Highscore: {self.highscore}", font=FONT)

    # Resets high score within the game loop
    def reset_score(self):
            if self.score > self.highscore:
                self.highscore = self.score
                with open("highscore.txt", "w") as file:
                    file.write(str(self.highscore))
            self.score = 0
            self.score_update()

    # If the snake has a collision it prints game over
    # def collision(self):
    #     self.setposition(-65, 0)
    #     self.write(";-; Game Over ;-;\n Click anywhere to try again.", font=FONT)