from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]


brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print(f"Your final score is {brain.print_score()}")
