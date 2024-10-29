from tkinter import *
import requests
import random

last_image = "./images/02.png"

def get_dadvice():
    global last_image
    photo_list = ["./images/01.png", "./images/02.png", "./images/03.png", "./images/04.png", "./images/05.png", "./images/07.png", "./images/08.png"]
    response = requests.get(url = 'https://api.adviceslip.com/advice')
    response.raise_for_status()
    advice = response.json()['slip']['advice']
    canvas.itemconfig(quote_text, text = advice)
    
    new_img = last_image
    while new_img == last_image:
        new_img = random.choice(photo_list)

    new_img = PhotoImage(file=random.choice(photo_list))
    dad_button.config(image=new_img)
    dad_button.image = new_img

window = Tk()
window.title("Dad Advice")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Dadvice, the best advice a from an internet dad!", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

dad_img = PhotoImage(file="./images/02.png")
dad_button = Button(image=dad_img, highlightthickness=0, command=get_dadvice)
dad_button.grid(row=1, column=0)

window.mainloop()