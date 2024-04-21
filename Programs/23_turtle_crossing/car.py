# Import relevant libraries
from turtle import Turtle
from random import randint

# Paddle class
class Car():

    # Initializing the turtle
    def __init__(self):
        self.cars = []
        self.car_speed = 0.1

    def make_cars(self):
        car = Turtle()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.shape("square")
        car.color((randint(3, 255), randint(3, 255), randint(3, 255)))
        car.setposition(400 , randint(-250, 250))
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(10)

    def increase_speed(self):
        self.car_speed *= 0.9

