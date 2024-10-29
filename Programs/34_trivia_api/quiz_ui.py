import tkinter as tk
from quiz_brain import QuizBrain
import data_quiz

PALE_YELLOW = "#F5EFE6"
BLUE = "#BCD2E8"
RED = "#ff746c"
GREEN = "#80ef80"

class QuizUI:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Millionaire Maker")
        self.window.configure(bg=PALE_YELLOW, padx= 30, pady= 30)
        self.window.geometry("500x650")


        self.score_label = tk.Label(text = "Score: "+ str(self.quiz.score), bg=PALE_YELLOW, fg="#000000", font = ("Courier New", 18, "bold")) 
        self.score_label.grid(row = 1, column = 1, padx = 20, pady = 20, columnspan = 2, sticky = "E")

        self.canvas = tk.Canvas(self.window, bg=BLUE, width = 400 , height = 335, highlightthickness = 0)
        self.q_text = self.canvas.create_text(200, 150, width = 350, text = "", fill = "#000000", font = ("Courier New", 30, "bold"), anchor = "center")
        self.canvas.grid(row = 2, column = 1, columnspan = 2, pady = 20, padx = 20)

        self.right_photo = tk.PhotoImage(file = "./images/right.png")
        self.right_button = tk.Button(image = self.right_photo, highlightthickness=0, borderwidth=0, command = self.right_button_clicked)
        self.right_button.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')

        self.wrong_photo = tk.PhotoImage(file = "./images/wrong.png")
        self.wrong_button = tk.Button(image = self.wrong_photo, highlightthickness=0, borderwidth=0, command = self.wrong_button_clicked)
        self.wrong_button.grid(row = 3, column = 2, padx = 20, pady = 10, sticky = 'w')

        self.next_question_canvas()

        self.window.mainloop()

    def next_question_canvas(self): 
        if self.quiz.questions_remaining():
            question_text = self.quiz.next_question()
            self.canvas.config(bg=BLUE)
            self.canvas.itemconfig(self.q_text, text=question_text)
        else: 
            self.canvas.itemconfig(self.q_text, text = f"You completed the quiz! \n Your final score is {self.quiz.score}.")
            self.canvas.config(bg=BLUE)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_clicked(self):
        right_ans = self.quiz.check_answer("True")
        self.give_feedback(right_ans)

    def wrong_button_clicked(self):
        right_ans = self.quiz.check_answer("False")
        self.give_feedback(right_ans)

    def give_feedback(self, right_ans):
        if right_ans == True:
            self.canvas.config(bg = GREEN)
            self.score_label.config(text = "Score: "+ str(self.quiz.score))
        else: 
            self.canvas.config(bg = RED)
        self.window.after(1000, self.next_question_canvas)

        

