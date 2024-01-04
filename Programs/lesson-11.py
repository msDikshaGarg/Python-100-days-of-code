import random
import os

art = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/      \n\n  
"""
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck_art = {
    11: '''
    .------.
    |A /\  |
    | /  \ |
    | \  / |
    |  \/ A|
    `------'
    ''', 
    2: '''
    .------.
    |2 /\  |
    | /  \ |
    | \  / |
    |  \/ 2|
    `------'
    ''', 
    3: '''
    .------.
    |3 /\  |
    | /  \ |
    | \  / |
    |  \/ 3|
    `------'
    ''', 
    4: '''
    .------.
    |4 /\  |
    | /  \ |
    | \  / |
    |  \/ 4|
    `------'
    ''', 
    5: '''
    .------.
    |5 /\  |
    | /  \ |
    | \  / |
    |  \/ 5|
    `------'
    ''', 
    6: '''
    .------.
    |6 /\  |
    | /  \ |
    | \  / |
    |  \/ 6|
    `------'
    ''', 
    7: '''
    .------.
    |7 /\  |
    | /  \ |
    | \  / |
    |  \/ 7|
    `------'
    ''', 
    8: '''
    .------.
    |8 /\  |
    | /  \ |
    | \  / |
    |  \/ 8|
    `------'
    ''', 
    9: '''
    .------.
    |9 /\  |
    | /  \ |
    | \  / |
    |  \/ 9|
    `------'
    ''', 
    10: ['''
    .------.
    |10/\  |
    | /  \ |
    | \  / |
    |  \/10|
    `------'
    ''',
    '''
    .------.
    |J /\  |
    | /  \ |
    | \  / |
    |  \/ J|
    `------'
    ''',  
    '''
    .------.
    |Q /\  |
    | /  \ |
    | \  / |
    |  \/ Q|
    `------'
    ''', 
    '''
    .------.
    |K /\  |
    | /  \ |
    | \  / |
    |  \/ K|
    `------'
    ''']
}
play_again = True

def random_card():
    card = random.choice(deck)
    return card

def calc_total(original_cards):
    return sum(original_cards)

def select_init():
    player.append(random_card())
    player.append(random_card())
    return player

def print_art(card):
    if card == 10:
        print(random.choice(deck_art[10]))
    else:
        print(deck_art[card])

def new_hand(original_cards, card):
    if card == 11 and calc_total(original_cards) > 10:
        original_cards.append(1)
    else:
        original_cards.append(card)
    return original_cards

bank = 500

while play_again == True:
    game_over = False
    hit = True
    dealer = []
    player = []
    
    print(art)

    while game_over != True:   
        print(f"You have $ {bank} in your account.")
        user_bet = int(input("How much do you want to bet?\n")) 
        while user_bet % 10 != 0:
                user_bet = int(input("Please enter bets in multiples of 10.\n"))

        player = select_init()
        print_art(player[0])
        print_art(player[1])
        print(f"Your cards are: {player}, current total is {calc_total(player)}")
        if calc_total(player) == 21:
            print("You win!")
            bank += user_bet
            game_over = True
            break
        else:
            new_card = random_card()
            new_hand(dealer, new_card)
            print_art(dealer[0])
            print(f"The dealer's hand: {dealer}")
            
        while hit != False:
            another = input("Would you like to hit or stand?\n").lower()
            if another == 'hit':
                new_card = random_card()
                print_art(new_card)
                new_hand(player, new_card)
                print(f"Your cards are: {player}, current total is {calc_total(player)}")
                if calc_total(player) > 21:
                    print("That's a bust.")
                    bank -= user_bet
                    game_over = True
                    break
                elif calc_total(player) == 21:
                    print("You win!")
                    bank += user_bet
                    game_over = True
                    break
            else: 
                hit = False
        if game_over == True:
            break
        else: 
            while calc_total(dealer) < 17:
                new_card = random_card()
                print_art(new_card)
                new_hand(dealer, new_card)
            print(f"The dealer's hand: {dealer}")
            player_total = calc_total(player)
            dealer_total = calc_total(dealer)
            print(f"Your total is {player_total} and the dealer's total is {dealer_total}.")

            if dealer_total > 21:
                print("Dealer goes bust. You win!")
                bank += user_bet
            elif player_total == dealer_total:
                print("It's a tie!")
            elif player_total > dealer_total: 
                print("You win.")
                bank += user_bet
            else: 
                print("Dealer wins.")
                bank -= user_bet
        game_over = True
    print(f"You have $ {bank} in your account now.")
    again = input("Type 'Yes' to play again or 'No' to exit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        play_again = False
    else: 
        os.system('clear')
