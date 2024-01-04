import random
import os

# Greeting
art = """
 _   _                                         
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/             \n\n
Let's play hangman!
"""

# Hangman art stages
hangman_stages = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

# Random word list
hangman_words = [
    'apple', 'banana', 'orange', 'grape', 'lemon', 'peach', 'melon', 'kiwi', 'plum',
    'carrot', 'broccoli', 'tomato', 'potato', 'onion', 'pepper', 'celery', 'cucumber', 'lettuce',
    'rabbit', 'turtle', 'parrot', 'hamster', 'giraffe', 'zebra', 'lion', 'tiger', 'elephant',
    'penguin', 'panda', 'koala', 'kangaroo', 'dolphin', 'whale', 'shark', 'octopus', 'seagull',
    'guitar', 'piano', 'violin', 'trumpet', 'flute', 'drums', 'saxophone', 'clarinet', 'banjo',
    'mountain', 'ocean', 'desert', 'forest', 'river', 'canyon', 'valley', 'island', 'volcano',
    'sunflower', 'rose', 'tulip', 'daisy', 'lily', 'carnation', 'orchid', 'peony', 'daffodil',
    'butterfly', 'dragonfly', 'firefly', 'ladybug', 'caterpillar', 'mosquito', 'spider', 'ant', 'beetle',
    'chocolate', 'vanilla', 'strawberry', 'caramel', 'peanut', 'coconut', 'almond', 'hazelnut', 'raspberry',
    'football', 'basketball', 'soccer', 'tennis', 'baseball', 'volleyball', 'golf', 'swimming', 'cycling',
    'computer', 'keyboard', 'mouse', 'monitor', 'printer', 'scanner', 'laptop', 'tablet', 'smartphone',
    'unicorn', 'mermaid', 'dragon', 'wizard', 'vampire', 'zombie', 'werewolf', 'ghost', 'witch',
    'diamond', 'emerald', 'sapphire', 'ruby', 'amethyst', 'topaz', 'opal', 'pearl', 'jade',
    'umbrella', 'raincoat', 'boots', 'scarf', 'gloves', 'sunglasses', 'hat', 'jacket', 'backpack',
    'whistle', 'compass', 'flashlight', 'binoculars', 'map', 'rope', 'knife', 'canteen', 'tent',
    'bicycle', 'motorcycle', 'airplane', 'helicopter', 'submarine', 'rocket', 'train', 'carriage', 'truck',
    'ancient', 'medieval', 'renaissance', 'baroque', 'romantic', 'impressionist', 'modern', 'contemporary', 'abstract',
    'science', 'biology', 'chemistry', 'physics', 'astronomy', 'geology', 'mathematics', 'psychology', 'sociology',
    'coffee', 'tea', 'espresso', 'latte', 'cappuccino', 'mocha', 'americano', 'chai', 'matcha'
]

play_again = True

while play_again == True:
    print(art)
    # Selecting a random word from word list
    word = list(random.choice(hangman_words))
    len_word = len(word)
    # Generating a blank word to be filled by the user
    user = list('_' * len_word)
    print(''.join(user))
    # Generating a list that displays the letters the user has already guessed (for good UI)
    guessed = []

    # Variables to keep track of lives and stage which the user is at
    lives = 6
    stage = 0

    # Game over flag
    game_over = False

    # While game is not over
    while game_over != True:
        # Asking user to guess a letter
        guess = input("Guess a letter:\n").lower()
        # Adding to guessed list and printing the list
        guessed.append(guess)
        print(f"You have already guessed: {guessed}")
        # Checking if the letter is in the word, if yes then adding it to print it 
        if guess in word:
            for i in range(0,len_word):
                if word[i] == guess:
                    user[i] = guess
        else:
            # Else the user looses lives
            lives -= 1
            stage += 1
        print(''.join(user))
        print(hangman_stages[stage])

        # When all lives are lost game over flag becomes true and the user loses and word is displayed
        if lives == 0:
            game_over = True
            print("Sorry, you lose. Try again.")
            print(f"Your word was '{''.join(word)}'.")

        # When no blanks remain the game is automatically over and user wins
        if '_' not in user:
            game_over = True
            print("You are a hangman champion!")

    again = input("Type 'Yes' to play again or 'No' to exit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        play_again = False
    else: 
        os.system('clear')