# Greeting art
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
