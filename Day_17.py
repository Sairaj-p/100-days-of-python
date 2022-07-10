# Quiz using OOP

from Day_17_Questions import question_data,logo
from random import randint
import os

#Declaring the Qustions
class Question():
    def __init__(self,no):
        self.text = question_data[no]["text"]
        self.ans = question_data[no]["answer"]
    

#Quiz Machine
class Quiz():
    def __init__(self,Qlist) -> None:
        self.Qlist = Qlist
        self.question_no =0
        self.Question_list =[]
        self.track = 0
        while self.track<len(Qlist):
            no = randint(0,len(Qlist)-1)
            if not no in self.Question_list:
                self.Question_list.append(no)
                self.track += 1
        

    def next_question(self):
        self.Q_no = self.Question_list[self.question_no]
        ans =f"\n-{self.Qlist[self.Q_no].q}"
        self.question_no += 1
        return ans
        

    def check_answer(self,answer:str):
        if answer == self.Qlist[self.Q_no].ans:
            return True
        else:
            return False
    def Question_no(self):
        return self.question_no


#Quiz Brain
def main():
    question_bank=[]
    for no in range(len(question_data)):
        new_q = Question(no)
        question_bank.append(new_q)
    os.system("cls")
    print(logo)
    print("Welcome to the Quiz Show")
    lenght = int(input("Enter the Lenght of the Quiz:"))
    quiz = Quiz(question_bank,lenght)
    cont = True
    Q_Count =0
    while cont and Q_Count<lenght:
        ans = quiz.next_question()
        cont = quiz.check_answer(ans)
        if cont:
            Q_Count += 1
        else:
            print("\n  Worng Answer \n   Game Over  \n")
    if cont:
        print("\nCongratulation you have Won!!!\n")

if __name__ == '__main__':
    main()     