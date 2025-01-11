#TODO: asking the question
#TODO: checking if the answer was correct
#TODO: checking if we're at the end of the quiz


#Q.1: A slug's blood is green. (True/False)?: 
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(answer, current_question.answer)
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That is incorrect")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")
