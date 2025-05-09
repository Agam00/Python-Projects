from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:


    def __init__(self,quiz_brain :QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.label=Label(text="Score: 0",bg=THEME_COLOR,fg="white",font=("Arial", 15))
        self.label.grid(row=0,column=1)

        self.can=Canvas(height=250,width=300)
        self.question_text=self.can.create_text(150,125,text="hey",font=('Arial',20,'italic'),width=280)
        self.can.grid(column=0,row=1,columnspan=2,pady=50)

        right_img=PhotoImage(file="./images/true.png")
        self.right_btn=Button(image=right_img,highlightthickness=0,command=self.correct,bd=0,bg=THEME_COLOR)
        self.right_btn.grid(column=0,row=2)

        wrong_img=PhotoImage(file="./images/false.png")
        self.wrong_btn=Button(image=wrong_img,highlightthickness=0,command=self.wrong,bd=0,bg=THEME_COLOR)
        self.wrong_btn.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.can.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.can.itemconfig(self.question_text,text=q_text)
        else:
            self.can.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
    def correct(self):
        self.feedback(self.quiz.check_answer("True"))
    def wrong(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self,is_right):
        if is_right:
            self.can.config(bg="green")


        else:
            self.can.config(bg="red")
        self.window.after(1000, self.get_next_question)



