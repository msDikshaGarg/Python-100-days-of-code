import tkinter as tk
import pandas as pd
import random

# Color palette
DARK_GREEN = "#32620E"
LIGHT_GREEN = "#C9DBB2"
PALE_YELLOW = "#F5EFE6"
curr_word = {}
after = None
revise = []

# Importing data and saving to a list of dictionaries
col_names = ["spanish", "english"]
try:
    all_words = pd.read_csv("./data/need_to_learn.csv", names =col_names)
except FileNotFoundError:
    all_words = pd.read_csv("./data/spanish_words.csv", names =col_names)
finally:
    all_words_list = all_words.to_dict(orient = "records")

# Saving the unknown words to a different file
def if_right():
    global curr_word, after, revise
    all_words_list.remove(curr_word)
    all_words = pd.DataFrame(all_words_list)
    revise = pd.DataFrame(revise)
    revise = pd.concat([revise, pd.DataFrame([curr_word])], ignore_index=True)
    all_words.to_csv("./data/need_to_learn.csv")
    revise.to_csv("./data/revise.csv")
    random_word()

# Getting a new word - main logic
def random_word():
    global curr_word, after
    window.after_cancel(after)
    curr_word = random.choice(all_words_list)
    canvas_main.itemconfig(title_text, text = "Spanish", fill = DARK_GREEN)
    canvas_main.itemconfig(word_text, text = f"{curr_word['spanish']}", fill = DARK_GREEN)
    canvas_main.itemconfig(image_current, image = front_photo)
    after = window.after(5000, func= show_translation)
    
# Changing to translation
def show_translation():
    canvas_main.itemconfig(image_current, image = back_photo)
    canvas_main.itemconfig(title_text, text = "English", fill = LIGHT_GREEN)
    canvas_main.itemconfig(word_text, text = f"{curr_word['english']}", fill = LIGHT_GREEN)

# window
window = tk.Tk()
window.title("Spanish Flash Cards")
window.configure(bg=PALE_YELLOW, padx= 30, pady= 30)
window.geometry("550x650")

after = window.after(5000, func= show_translation)

# Heading label
spanish_label = tk.Label(text = "Let's learn spanish!", bg=PALE_YELLOW, fg=DARK_GREEN, font = ("Courier New", 40, "bold"))
spanish_label.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)

# Main flashcard image
canvas_main = tk.Canvas(window, width = 260 , height = 335, highlightthickness = 0)
front_photo = tk.PhotoImage(file = "./images/front.png")
back_photo = tk.PhotoImage(file = "./images/back.png")
image_current = canvas_main.create_image(130, 167, image = front_photo)
title_text = canvas_main.create_text(130, 120, text = "", fill = DARK_GREEN, font = ("Courier New", 20, "bold"))
word_text = canvas_main.create_text(130, 170, text = "", fill = DARK_GREEN, font = ("Courier New", 30, "bold"))
canvas_main.grid(row = 2, column = 1, columnspan = 2, pady = 10)

# Right button
right_photo = tk.PhotoImage(file = "./images/right.png")
right_button = tk.Button(image = right_photo, highlightthickness=0, borderwidth=0, command= if_right)
right_button.grid(row = 3, column = 1, padx = 30, pady = 10, sticky = 'e')

# Wrong button
wrong_photo = tk.PhotoImage(file = "./images/wrong.png")
wrong_button = tk.Button(image = wrong_photo, highlightthickness=0, borderwidth=0, command = random_word)
wrong_button.grid(row = 3, column = 2, padx = 30, pady = 10, sticky = 'w')

random_word()

window.mainloop()

