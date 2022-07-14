#Quiz app gui

import requests
from Day_17 import Quiz
from tkinter import *

theme_color ="#375362"
parameters = {
"amount":10,
"category":18,
"type":"boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
question_data =data['results']

class Questions():
    def __init__(self,no):
        self.q = question_data[no]["question"]
        self.ans = question_data[no]["correct_answer"]

class QuizInterface():
    def __init__(self,quiz:Quiz):
        self.Question_no =0
        self.quiz = quiz
        self.c_score =0
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,bg=theme_color)
        self.score_l = Label(text=f"Score:{self.c_score}",bg =theme_color,fg="white")
        self.canvas = Canvas(height=250,width=300)
        self. Qusetion =self.canvas.create_text(150,125,text="Question",fill=theme_color,
        font=("Arial",10,"italic"),width=250)
        correct_b_img =PhotoImage(file=r"E:\New folder\Flash Card\images\right.png")
        wrong_b_img =PhotoImage(file=r"E:\New folder\Flash Card\images\wrong.png")
        
        self.True_button = Button(image=correct_b_img,highlightthickness=0,background=theme_color,command=self.True_ans)
        self.False_button = Button(image=wrong_b_img,highlightthickness=0,background=theme_color,command=self.False_ans)
        self.score_l.grid(row=0,column=1)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.True_button.grid(row=2,column=0,pady=20,padx=20)
        self.False_button.grid(row=2,column=1,pady=20,padx=20)
        self.next_question_inter()
        self.window.mainloop()

    def next_question_inter(self):
        if self.Continue_nq():
            self.Question_no += 1
            self.canvas.config(bg="white")
            self.score_l.config(text=f"Score:{self.c_score}")
            self.new_q = self.quiz.next_question()
            self.canvas.itemconfig(self.Qusetion,text=self.new_q)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.Qusetion,text=f"The Quiz Is Finished\nYour Score :{self.c_score}")
            self.True_button.config(state="disabled")
            self.False_button.config(state="disabled")

    def True_ans(self):
        self.ans = self.quiz.check_answer("True")
        self.Check_ans(self.ans)
        
    def False_ans(self):
        self.ans = self.quiz.check_answer("False")
        self.Check_ans(self.ans)

    def Check_ans(self,ans):
        if ans == True:
            self.c_score += 1
            self.canvas.config(bg="green")
            
            self.window.after(1000,self.next_question_inter)     
        else:
            self.canvas.config(bg ="red")
            self.window.after(1000,self.next_question_inter)  

    def Continue_nq(self):
        if self.quiz.Question_no() < 10:
            return True
        else:
            return False    

        
ques_bank =[]
for _ in range(0,10):
    ques_bank.append(Questions(_))
quiz = Quiz(ques_bank)
interface = QuizInterface(quiz)
