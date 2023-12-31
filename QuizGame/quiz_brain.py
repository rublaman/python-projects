from QuizGame.question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_number: int = 0
        self.question_list: list[Question] = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\tYou got it right!")
        else:
            print("That a wrong answer!")

        print(f"\tYour current score is: {self.score}/{self.question_number}\n")
