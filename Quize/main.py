from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    new_question = Questions(questions["text"], questions["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'''You've completed the quiz 
Your final score was : {quiz.score}/{quiz.question_number}''')