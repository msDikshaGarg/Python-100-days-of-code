from turtle import Turtle

# Net class (100% Skip-able)
class Net(Turtle):

    # Initializing the turtle 
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#DDA0DD")
        self.penup()
        self.net()

    # Just making a dashed line to give the illusion of a net across the pong table 
    def net(self):    
        self.goto(0,-230)
        self.left(90)
        self.pensize(4)
        for _ in range(12):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)