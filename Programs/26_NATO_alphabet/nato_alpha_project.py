import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_data_dict = { row.letter : row.code for index, row in nato_data.iterrows()}

def gen_list():
    word = input("What is your word?\n").upper()
    try:
        word_list = [nato_data_dict[alpha] for alpha in word]
    except KeyError:
        print("Invalid input: Please enter alphabets only.")
        gen_list()
    else:
        print(word_list)

gen_list()