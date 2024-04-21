# Importing the relevant classes and files 
from turtle import Screen
import time
import random
from turtle_player import Voldetort
from score import Score
from car import Car

# Initializing screen 
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("Black")
screen.title("Crossing Game")
screen.colormode(255)
screen.tracer(0)

game_on = True

player_turtle = Voldetort()
score = Score()
car = Car()

while game_on:
    screen.update()
    time.sleep(car.car_speed)
    screen.listen()
    screen.onkey(key="Up", fun=player_turtle.up)
    
    rand_chance = random.randint(0,3)
    if rand_chance == 2:
        car.make_cars()
    car.move()

    if player_turtle.ycor() > 290:
        player_turtle.reset()
        score.update_score()
        car.increase_speed()

    for i in car.cars:
        if player_turtle.distance(i) < 20: 
            score.game_over()
            game_on = False

# When the screen is clicked after a game is over the screen goes away
screen.exitonclick()