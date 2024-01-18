# Quiz

![Quiz](../../GIFs/giphy_who_wants_2b_a_millionaire.gif)

You are on a game show called Millionaire Maker, where getting the right answers won't get you a million dollars but will definitely get you even more precious 'bragging rights'!

This program used Object Oriented Programming.

### Data
The data file contains the quiz question and answer data. For more you can visit [Open Trivia Database](https://opentdb.com/).

### Question Model
The question model file contains the Question class where attributes of a question are initialized, the text and the answer to the question.

### Quiz Brain
The quiz brain file initializes the current question number, question list that we are using for the quiz and score. The `questions_remaining()` method checks if there are questions remaining in the quiz, returns False if there are no questions remaining. The `next_question()` method takes the current question and using the question text, asks the player the question and takes their input as an answer. Then passes the input and the actual answer to the `check_answer()` method which checks if the answer is correct and prints the feedback along with the current score.

### Main
The main file imports the classes and makes the question bank by looping through the question data using the Question class. Then it creates a new object using Quiz Brain and asks the next questions till the questions remain. Once the quiz ends, it prints the final score. 