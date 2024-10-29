class QuizBrain:

    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0
        self.current_ques = None

    # Function that checks if the quiz has questions remaining
    def questions_remaining(self):
        return self.question_number < len(self.question_list)

    # Function that prints the current question and calls the check function to check for the correct answer
    def next_question(self):
        self.current_ques = self.question_list[self.question_number]
        self.question_number+=1
        return f"Q.{self.question_number} : {self.current_ques.text}."

    # Function that checks if the user answer is correct and prints out the current score
    def check_answer(self, user_ans):
        if self.current_ques:
            correct_ans = self.current_ques.answer
            if user_ans == correct_ans:
                self.score += 1
                return True
            else: 
                return False
        