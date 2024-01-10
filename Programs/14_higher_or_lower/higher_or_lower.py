import random
from data.data_higher_lower import data
import os
from artwork import art

game_over = False

def maximum(num1,num2):
    if num1 > num2:
        return num1
    else: 
        return num2

while game_over == False:
    print(art)
    A = random.choice(data)
    win = True
    score = 0
    
    while win == True:
        B = random.choice(data)
        while A == B:
            B = random.choice(data)
        print(f"Compare A : {A['name']}, a {A['description']}, from {A['country']}.\n")
        print("VS\n")
        print(f"Against B : {B['name']}, a {B['description']}, from {B['country']}.\n")
        
        guess = input("Who has more followers? Type 'A' or 'B'.\n").upper()
        while guess not in ['A', 'B']:
            guess = input("Type 'A' or 'B'.\n").upper()
        if guess == 'A':
            guess = A['follower_count']
        else:
            guess = B['follower_count']

        answer = max(A['follower_count'], B['follower_count'])
        if answer == guess:
            score += 1
            A = B
            print(f"\n\nCorrect answer! Your score is: {score}.\n\n")
        else: 
            print(f"\n\nWrong answer! Your final score is: {score}.\n\n")
            win = False
    
    again = input("Would you like to try again? Yes or no.\n").lower()
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        game_over = True