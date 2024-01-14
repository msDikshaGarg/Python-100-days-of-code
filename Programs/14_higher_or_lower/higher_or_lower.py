# Importing relevant libraries and files
import random
from data_higher_lower import data
from artwork import art

game_over = False

# Checking the higher follower count
def maximum(num1,num2):
    if num1 > num2:
        return num1
    else: 
        return num2

while game_over == False:
    # Starting with initializing the first account
    print(art)
    A = random.choice(data)
    win = True
    score = 0
    # While the player is winning 
    while win == True:
        # Choose the second account to compare
        B = random.choice(data)
        # If both choices are same then generate a new choice
        while A == B:
            B = random.choice(data)

        # Displaying the choices to the player
        print(f"Compare A : {A['name']}, a {A['description']}, from {A['country']}.\n")
        print("VS\n")
        print(f"Against B : {B['name']}, a {B['description']}, from {B['country']}.\n")
        
        #Taking the player guess
        guess = input("Who has more followers? Type 'A' or 'B'.\n").upper()
        # if guess is not valid then ask again
        while guess not in ['A', 'B']:
            guess = input("Type 'A' or 'B'.\n").upper()
        # Get follower counts for the guess
        if guess == 'A':
            guess = A['follower_count']
        else:
            guess = B['follower_count']

        # Check which follower count is higher
        answer = max(A['follower_count'], B['follower_count'])
        # If the player guesses correctly, one point is added and option B becomes option A
        if answer == guess:
            score += 1
            A = B
            print(f"\n\nCorrect answer! Your score is: {score}.\n\n")
        else: 
            # Otherwise the player loses and the game ends
            print(f"\n\nWrong answer! Your final score is: {score}.\n\n")
            win = False
    
    # Give the player an option to try again
    again = input("Would you like to try again? Yes or no.\n").lower()
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        game_over = True