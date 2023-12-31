from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")
placeholder = "The quick brown fox jumps over the lazy dog"
score = 0


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text=placeholder, font=FONT,
            fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=tick_image, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightbackground=THEME_COLOR, command=self.false_pressed)
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
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        user_answer_t = "true"
        is_right = self.quiz.check_answer(user_answer_t)
        self.give_feedback(is_right)

    def false_pressed(self):
        user_answer_f = "false"
        is_right = self.quiz.check_answer(user_answer_f)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    # # Type hints *** just an example
    # def greeting(self, name: str) -> str:
    #     return "hello" + name
