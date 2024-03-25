from turtle import Turtle

# Score class
class Score(Turtle):

    # Initializing turtle properties to write text on screen
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#DDA0DD")
        self.penup()
        self.r_score = 0
        self.l_score = 0 
        self.update_score()

    # Writing the score for the left player
    def update_l_score(self):
        self.l_score +=1
        self.update_score()

    # Writing the score for the right player
    def update_r_score(self):
        self.r_score +=1
        self.update_score()

    # Updating the scores as the game goes on
    def update_score(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align = "center", font=("Arial", 80, 'normal'))
        self.goto(100, 150)
        self.write(self.r_score, align = "center", font=("Arial", 80, 'normal'))

    # Printing the winner names after the game is over
    def game_over(self):
        self.setposition(-65, 0)
        self.write("Game Over", font = ('Arial', 24, 'normal'))
        self.goto(-65, -20)
        if self.l_score > self.r_score:
            self.write("Player 2 wins.", font = ('Arial', 24, 'normal'))
        else: 
            self.write("Player 1 wins.", font = ('Arial', 24, 'normal'))