#Rock Paper Scissor game

import random
from re import U

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
computer_choice= random.randint(0,3)
print("Welcom to Rock paper scissor Game")
user_choice = int(input("0-Rock , 1-paper, 2- scissor\n:"))
if user_choice>2 or user_choice<0:
    print("invalid input:")
else:
    print("\n\nYour Choice is:\n",game[user_choice])
    print("\n \nComputer choice is :\n",game[computer_choice])

    #Brain of the game
    if(user_choice == computer_choice):
        print("It is a tie")
    elif(user_choice == computer_choice+1):
        print("You wins!")
    elif(computer_choice == user_choice+1):
        print("Computer wins!")
    elif computer_choice==2 and user_choice==0:
        print("You win!")
    else:
        print("Computer wins!")
