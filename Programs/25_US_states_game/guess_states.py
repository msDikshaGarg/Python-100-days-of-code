import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("/Users/dikshagarg/Desktop/Python 100 days of code/Programs/25_US_states_game/50_states.csv")
to_guess = list(states_data["state"])

while len(to_guess) > 0:
    new_state = screen.textinput(title=f"{50 - len(to_guess)}/50 States Correct",prompt="Guess a state!").title()

    if new_state == 'Exit':
        not_guessed = pd.DataFrame(to_guess)
        not_guessed.to_csv("not_guessed.csv")
        break
    
    if new_state in to_guess:
        to_guess.remove(new_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        selected_state = states_data[states_data["state"]==new_state]
        state_turtle.goto(int(selected_state['x']), int(selected_state['y']))
        state_turtle.write(new_state.capitalize())

if not to_guess:
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(-100, 0)
    state_turtle.write("Yay, you guessed all the states!", font=("Arial", 24, 'normal'))

     