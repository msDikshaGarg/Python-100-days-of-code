# Importing relevant libraries and files
import random
import os
from artwork import art, deck_art

# Defining the deck
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Play again flag
play_again = True

# Function to pick a random card from the deck
def random_card():
    card = random.choice(deck)
    return card

# Function to calculate the total for the cards in hand
def calc_total(original_cards):
    return sum(original_cards)

# Function to select the first 2 random cards for the player
def select_init():
    player.append(random_card())
    player.append(random_card())
    if player[0] == player [1] == 11:
        player[1] = 1
    return player

# Function to print the corresponding card art for the pulls
def print_art(card):
    if card == 10:
        print(random.choice(deck_art[10]))
    else:
        print(deck_art[card])

# Function to display the new cards in hand with each pull
def new_hand(original_cards, card):
    if card == 11 and calc_total(original_cards) > 10:
        original_cards.append(1)
    else:
        original_cards.append(card)
    return original_cards

bank = 500

# while the player wants to keep playing 
while play_again == True:
    # Initialise each variable with each new game 
    game_over = False
    hit = True
    dealer = []
    player = []
    # Print the greeting art
    print(art)
    # While game is not over and nobody has won
    while game_over != True: 
        # Ask player for the amount they want to bid  
        print(f"You have $ {bank} in your account.")
        user_bet = float(input("How much do you want to bet?\n")) 
        # The bids are only allowed in multiples of 10
        while user_bet > bank:
            user_bet = int(input("Sorry, you are trying to bet more money than you actually have. Try again with a lower bet or visit an ATM.\n"))

        # Run function for inital cards and print art
        player = select_init()
        print_art(player[0])
        print_art(player[1])
        print(f"Your cards are: {player}, current total is {calc_total(player)}")
        # If the player gets 21 then player automatically wins and game is over, player wins
        if calc_total(player) == 21:
            print("You win!")
            bank = bank + 1.5 * user_bet
            game_over = True
            break
        else:
            # Else the dealer pulls a card and dealer's hand is displayed
            new_card = random_card()
            new_hand(dealer, new_card)
            print_art(dealer[0])
            print(f"The dealer's hand: {dealer}")
        # If the player wants to draw cards we give them the option and print the new hand with each draw   
        while hit != False:
            another = input("Would you like to hit or stand?\n").lower()
            if another == 'hit':
                new_card = random_card()
                print_art(new_card)
                new_hand(player, new_card)
                print(f"Your cards are: {player}, current total is {calc_total(player)}")
                # If player total reaches over 21, player goes bust and game is over, player loses 
                if calc_total(player) > 21:
                    print("That's a bust.")
                    bank = bank - user_bet
                    game_over = True
                    break
                # If player gets 21 player wins and game is over
                elif calc_total(player) == 21:
                    print("You win!")
                    bank = bank + 1.5 * user_bet
                    game_over = True
                    break
            else: 
                # Else the player stands
                hit = False
        if game_over == True:
            break
        else: 
            # If game is not over yet, the dealer draws cards till the total is less than 17
            while calc_total(dealer) < 17:
                new_card = random_card()
                print_art(new_card)
                new_hand(dealer, new_card)
            print(f"The dealer's hand: {dealer}")
            player_total = calc_total(player)
            dealer_total = calc_total(dealer)
            print(f"Your total is {player_total} and the dealer's total is {dealer_total}.")

            # Comparing the hand of the dealer we decide who won and game is over
            if dealer_total > 21:
                print("Dealer goes bust. You win!")
                bank = bank + 1.5 * user_bet
            elif player_total == dealer_total:
                print("It's a tie!")
            elif player_total > dealer_total: 
                print("You win.")
                bank = bank + 1.5 * user_bet
            else: 
                print("Dealer wins.")
                bank = bank - user_bet
        game_over = True
    if bank == 0:
        print("You lost all your money to gambling. 😣")
        print(f"You have $ {bank} in your account now.")
        break
    # Asks the player if they want to play anouther round
    print(f"You have $ {bank} in your account now.")
    again = input("Type 'Yes' to play again or 'No' to exit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        play_again = False
    else: 
        # If they say yes, clear and restart the game loop
        os.system('clear')
