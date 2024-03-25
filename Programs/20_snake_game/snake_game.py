# importing the relevant classes and files 
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time 

# Initializing screen 
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)


# Initializing the the no collision flag and all the objects from the classes
no_collision = True
food = Food()
snake = Snake()
score = Score()

# Checks which key is pressed and calls the appropriate function
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# Game loop
while no_collision:
    # Update screen every time a snake moves or a segment is added
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Eating food by checking distance with food, if the snake touches the food, the food gets moved to a new position. The score increases, a new segment is added and the updated score is printed
    if snake.first.distance(food) < 20:
        food.new_pos()
        score.score += 1
        score.score_update()
        snake.add_segment()
    
    # Collision with the wall if the snake touches the wall coordinate then collision flag is triggered and the game over message is printed
    if -290 < snake.first.xcor() < 290 and -290 < snake.first.ycor() < 290:
        pass
    else: 
        no_collision = False
        score.collision()

    # Collision with the snake, if the snake hits its own body then the game over flag is triggered
    for i in snake.segments[1:]:
        if snake.first.distance(i) < 10:
            no_collision = False
            score.collision()

# When the screen is clicked after a game is over the screen goes away
screen.exitonclick()
