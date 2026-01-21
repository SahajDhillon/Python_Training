from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    question_text = ques['text']
    question_ans = ques['answer']
    new_question = Question(q_text=question_text, q_ans=question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    ans = quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is : {quiz.total_marks}/{quiz.question_number}")
