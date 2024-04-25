# Reading the names
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.read()
# Splitting the names using the newline character and storing them in a list
name_list = names.split('\n')

# Reading the sample letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_sample = letter_file.read()

# For each name in the list, replacing the sample name with the actual name and storing the letter in individual text files
for name in name_list:
    letter = letter_sample.replace('[name]', name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w") as new_file:
        new_file.write(letter)
