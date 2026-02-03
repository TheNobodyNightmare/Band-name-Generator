from question_model import Question
from data import question_data
from quiz_brain import QuizBrian

question_Object = []
for question  in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_Object.append(new_question)

quiz = QuizBrian(question_Object)
while quiz.still_has_question():
    quiz.new_question()



