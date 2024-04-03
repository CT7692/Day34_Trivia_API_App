from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
MY_FONT = ("Arial", 15, "italic")
Y_PAD = 50

class QuizUI:
    def __init__(self, qb: QuizBrain):
        self.my_answer = ""
        self.quiz = qb
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f"Score: {self.quiz.score}",
                                bg=THEME_COLOR, fg="white", highlightthickness=0,
                                pady=Y_PAD, font=("Arial", 15))
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(
            150, 125,text="", font=MY_FONT, width=280, justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2)

        check = PhotoImage(file="images/true.png")
        x = PhotoImage(file="images/false.png")

        self.true = Button(image=check,
                           highlightthickness=0, command=self.choose_true)
        self.true.grid(column=0, row=2, pady=25)

        self.false = Button(image=x,
                            highlightthickness=0, command=self.choose_false)
        self.false.grid(column=1, row=2)
        self.get_new_question()
        self.window.mainloop()

    def get_new_question(self):
        if self.quiz.still_has_questions():
            self.enable_buttons()
            self.canvas.config(bg="white")
            q_line = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_line)
        else:
            messagebox.showinfo(
                title="You Finished",
                message=f"You've completed the quiz."
                    f"\nYour final score: {self.quiz.score}/{self.quiz.question_number}")
            self.window.quit()
    def choose_true(self):
        self.my_answer = "True"
        self.check_answer()

    def choose_false(self):
        self.my_answer = "False"
        self.check_answer()

    def check_answer(self):
        answer = self.quiz.current_question.answer
        if self.my_answer == answer:
            self.canvas.config(bg="green")
            self.disable_buttons()
            self.update_score()
        else:
            self.canvas.config(bg="red")
            self.disable_buttons()
        self.window.after(1000, self.get_new_question)

    def update_score(self):
        self.quiz.score += 1
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def enable_buttons(self):
        self.true.config(state="active")
        self.false.config(state="active")

    def disable_buttons(self):
        self.true.config(state="disabled")
        self.false.config(state="disabled")