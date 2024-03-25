# Importing the relevant classes and files 
from turtle import Screen
from net import Net
from paddle import Paddle
from score import Score
from ball import Ball
import time 

# Initializing variables
game_on = True
time_start = 0.1

# Initializing screen 
screen = Screen()
screen.setup(width= 800, height= 500)
screen.bgcolor("Black")
screen.title("Ping Pong")
screen.tracer(0)

# Making objects from classes
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score = Score()
net = Net()

# While game is running
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    # Listen for player inputs and move paddles accordingly
    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.up)
    screen.onkey(key="Down", fun=r_paddle.down)
    screen.onkey(key="w", fun=l_paddle.up)
    screen.onkey(key="s", fun=l_paddle.down)
    # Move the ball when game starts
    ball.move()
    
    # If Score reaches 11, the respective player wins and the game stops
    if score.l_score == 11 or score.r_score == 11:
        game_on = False
        break

    # If the ball hits the top or bottom of the screen, the ball bounces
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    # If the ball hits the right paddle or the left paddle, the ball bounces
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        time_start = ball.random_speed()
        ball.setx(340)
        ball.bounce_x()
    elif ball.distance(l_paddle) < 51 and ball.xcor() < -350:
        time_start = ball.random_speed()
        ball.setx(-350)
        ball.bounce_x()
    
    # If the right player misses the ball, the left player gets a point and vice versa
    if ball.xcor() > 390:
        ball.ball_reset()
        score.update_l_score()
        
    if ball.xcor() < -390:
        ball.ball_reset()
        score.update_r_score()

# Once the game is over the winner is declared 
score.game_over()

# When the screen is clicked after a game is over the screen goes away
screen.exitonclick()