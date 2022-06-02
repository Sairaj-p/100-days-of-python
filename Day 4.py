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
computer_choice= random.randint(0,3)
print("Welcom to Rock paper scissor Game")
user_choice = int(input("0-Rock , 1-paper, 2- scissor\n:"))

print("\n\nYour Choice is:")
if user_choice ==0:
    print(rock)
elif user_choice==1:
    print(paper)
elif user_choice == 2:
    print(scissors)
print("\n \nComputer choice is :")
if computer_choice ==0:
    print(rock)
elif computer_choice==1:
    print(paper)
elif computer_choice==2:
    print(scissors)

#Brain of the game
if(user_choice == computer_choice):
    print("It is a tie")
elif(user_choice == computer_choice+1):
    print("You wins!")
elif(computer_choice == user_choice+1):
    print("Computer wins!")
elif computer_choice==2 and user_choice==0:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("Computer wins!")
else:
    print("invalid input")
