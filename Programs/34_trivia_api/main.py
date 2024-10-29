# Importing relevant classes and files
from data_quiz import data
from question_model import Question
from quiz_brain import QuizBrain
import random
import html
from quiz_ui import QuizUI
#from category_ui import CategoryUI

# Initializing question bank
question_bank = []
ques_choice = []
play_again = True

#cat = CategoryUI()

# Looping through the questions to pick 10 questions
for q in range(0,10):
    # Chooses a random question from the list
    ques = random.choice(data["results"])
    ques_choice.append(ques)
    # If question is already chosen, chooses a new question
    while ques in ques_choice:
        ques = random.choice(data["results"])
    # Get's the question in the right format
    question = html.unescape(ques["question"])
    print(question)
    answer = ques["correct_answer"]
    # Adds question to the question bank using the Question class
    new_quiz_question = Question(question, answer)
    question_bank.append(new_quiz_question)

# Making a new quiz object
quiz = QuizBrain(question_bank)

face = QuizUI(quiz)

print("Welcome to Millionaire Maker. Let's see if you can win the quiz!\n")

# While there are questions remaining, call the next question
while quiz.questions_remaining():
    quiz.next_question()

# Print the final score once the quiz is over
print(f"The quiz is over. Your final score is: {quiz.score}/{quiz.question_number}")

# Prints a final statement to give the user bragging rights
if quiz.score < quiz.question_number:
    print("Sadly, you can't brag much about this. Try again.")
else: 
    print("Congratulations! You get all the bragging rights.")
        

