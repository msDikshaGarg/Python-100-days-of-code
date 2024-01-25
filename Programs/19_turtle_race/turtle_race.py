# Importing turtle 
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500 , height=400)

turtles = {"Peru" : "Crush", "Purple" : "Donatello", "OliveDrab": "Oogway", "DarkTurquoise" : "Squirtle", "Gold" : "Bowser"}

colors = ["Peru", "Purple", "OliveDrab", "DarkTurquoise", "Gold"]
start_y = [-100, -50, 0, 50, 100]
all_turtles = []

race_start = False

for i in range(0,5):
    new = Turtle(shape="turtle")
    new.color(colors[i])
    new.penup()
    new.goto(-230, start_y[i])
    all_turtles.append(new)

bet = screen.textinput(title="Let's bet", prompt="Which famous turtle will win? \n (Crush / Donatello / Oogway / Squirtle / Bowser)")

if bet:
    race_start = True

while race_start:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_start = False
            winner_color = turtle.color()
            winner = turtles[winner_color[0]]
            if bet == winner.lower():
                print(f"You won! The winner is {winner}!")
            else:
                print(f"You lost. The winner is {winner}.")
        turtle.forward(random.randint(0,10))

screen.exitonclick()