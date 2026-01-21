class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.total_marks = 0

    def still_has_questions(self):
        length = len(self.question_list)
        return self.question_number < length


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {current_question.text} (True/False) ? :").capitalize()
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, user_input):
        if user_input == answer:
            print("Your Answer is correct")
            self.total_marks += 1
        else:
            print("Your Answer is wrong")
        print(f"Your current score is: {self.total_marks}/{self.question_number}")
