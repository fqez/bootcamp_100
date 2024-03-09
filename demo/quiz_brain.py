import random


class QuizBrain:

    def __init__(self, list_of_questions):
        self.questions = list_of_questions
        random.shuffle(self.questions)
        self.question_number = 0
        self.score = 0


    def next_question(self):

        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)


    def still_has_questions(self):
        return self.question_number < len(self.questions)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer :(")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")


    def print_score(self):
        return f"{self.score}/{len(self.questions)}"