from pydoc import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0",
                                 fg="white",
                                 bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)


        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
                150,
                125, 
                width= 280,
                text="Question goes here.", 
                font=("Arial", 20, "italic"), 
                fill=THEME_COLOR
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_button_img = PhotoImage(file="./images/true.png")
        false_button_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_button_img, highlightthickness=0, bd=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        
        self.false_button = Button(image=false_button_img, highlightthickness=0, bd=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

