import pandas as pd

nato_data = pd.read_csv("/Users/dikshagarg/Desktop/Python 100 days of code/Programs/26_NATO_alphabet/nato_phonetic_alphabet.csv")

nato_data_dict = { row.letter : row.code for index, row in nato_data.iterrows()}

word = input("What is your word?\n").upper()
word_list = [nato_data_dict[alpha] for alpha in word if alpha in nato_data_dict]

print(word_list)