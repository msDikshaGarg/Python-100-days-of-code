class QuizBrain:

    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    # Function that checks if the quiz has questions remaining
    def questions_remaining(self):
        return self.question_number < len(self.question_list)

    # Function that prints the current question and calls the check function to check for the correct answer
    def next_question(self):
        current_ques = self.question_list[self.question_number]
        self.question_number+=1
        user_ans = input(f"Q.{self.question_number} : {current_ques.text} (True/False)?\n").lower()
        while user_ans not in ['true', 'false']:
            user_ans = input("Please enter a valid answer.").lower()
        self.check_answer(user_ans, current_ques.answer)

    # Function that checks if the user answer is correct and prints out the current score
    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            self.score += 1
            print("This is the correct answer!")
        else: 
            print(f"Sorry, that's incorrect. The correct answer was {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
        