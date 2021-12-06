from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in question_data:
    a = Question(i["text"], i["answer"])
    question_bank.append(a)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score} / {len(question_data)}")