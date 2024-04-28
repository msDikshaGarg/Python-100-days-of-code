import tkinter as tk
import pandas as pd

# Color palette
LIGHT_PINK = "#FFE6E6"
PINK = "#E1AFD1"
LAVENDER = "#AD88C6"
VIOLET = "#7469B6"

# Changing to translation
# def change_image():
#     global back_photo
#     back_photo = tk.PhotoImage(file = "./images/back.png")
#     canvas_main.itemconfig(image_current, image = back_photo)

all_words = pd.read_csv("./data/spanish-frequent-words.csv")
all_words_dict = all_words.to_dict(orient = "records")


# window
window = tk.Tk()
window.title("Spanish Flash Cards")
window.configure(bg=LIGHT_PINK, padx= 30, pady= 30)
window.geometry("650x500")

# Heading label
spanish_label = tk.Label(text = "Let's learn spanish!", bg=LIGHT_PINK, fg=LAVENDER, font = ("Courier New", 40, "bold"))
spanish_label.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)

# Main flashcard image
canvas_main = tk.Canvas(window, width = 576 , height = 256, highlightthickness = 0)
front_photo = tk.PhotoImage(file = "./images/front.png")
#back_photo = tk.PhotoImage(file = "./images/back.png")
image_current = canvas_main.create_image(288, 128, image = front_photo)
canvas_main.create_text(288, 120, text = "Title", fill = VIOLET, font = ("Courier New", 20, "bold"))
canvas_main.create_text(288, 170, text = "Word", fill = VIOLET, font = ("Courier New", 40, "bold"))
canvas_main.grid(row = 2, column = 1, columnspan = 2, pady = 10)

# Thumbs up image
thumb_up = tk.PhotoImage(file = "./images/thumbs_up.png")
thumbs_up_button = tk.Button(image = thumb_up, highlightthickness=0, borderwidth=0)
thumbs_up_button.grid(row = 3, column = 1, padx = 30, pady = 10, sticky = 'e')

# Thumbs down image
thumb_down = tk.PhotoImage(file = "./images/thumbs_down.png")
thumbs_down_button = tk.Button(image = thumb_down, highlightthickness=0, borderwidth=0)
thumbs_down_button.grid(row = 3, column = 2, padx = 30, pady = 10, sticky = 'w')

#canvas_main.bind("<Button-1>", change_image)

window.mainloop()

