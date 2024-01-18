# Importing data and classes 
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from artwork import art

# Initializing question bank
question_bank = []

play_again = True

# Looping through the questions in data and adding them to the question bank using the Question class
for q in question_data:
    question = q['text']
    answer = q['answer']
    new_quiz_question = Question(question, answer)
    question_bank.append(new_quiz_question)

# Making a new quiz object
quiz = QuizBrain(question_bank)

print(art)
print("Welcome to Millionaire Maker. Let's see if you can win the quiz!\n")

# While there are questions remaining, call the next question
while quiz.questions_remaining():
    quiz.next_question()

# Print the final score once the quiz is over
print(f"The quiz is over. Your final score is: {quiz.score}/{quiz.question_number}")

if quiz.score < quiz.question_number:
    print("Sadly, you can't brag much about this. Try again.")
else: 
    print("Congratulations! You get all the bragging rights.")
        

