from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    quest = Question(question["text"],question["answer"])
    question_bank.append(quest)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.get_next_question()
quiz.final_score()