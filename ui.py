from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150,
                                                     100,
                                                     text="example",
                                                     font=("Arial", 18, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)

        self.score_label = Label(text=f"score:{self.quiz.score}", font=("Arial", 14, "italic"), bg=THEME_COLOR, fg="white", height=2)
        self.score_label.grid(row=0, column=1)

        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, width=100, height=97, command=self.click_check_button)
        self.check_button.grid(row=2, column=1, pady=20)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, width=100, height=97, command=self.click_cross_button)
        self.cross_button.grid(row=2, column=0, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="You've reached the end of the quiz.")
            self.cross_button.config(state="disabled")
            self.check_button.config(state="disabled")

    def click_check_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_cross_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

