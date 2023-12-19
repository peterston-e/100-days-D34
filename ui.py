from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")
placeholder = "The quick brown fox jumps over the lazy dog"
score = 0


class QuizzInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {score}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text=placeholder, font=FONT,
            fill=THEME_COLOR, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=tick_image, highlightbackground=THEME_COLOR)
        self.true_button.grid(column=0, row=2)

        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightbackground=THEME_COLOR)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
