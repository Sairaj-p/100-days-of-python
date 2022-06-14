#Number Guessing Game /scope
import os
import random
NUMBER = random.randint(1,100)
game_end = False
logo ="""
  _______  __    __   _______     _______.     _______. __  .__   __.   _______      _______      ___      .___  ___.  _______ 
 /  _____||  |  |  | |   ____|   /       |    /       ||  | |  \ |  |  /  _____|    /  _____|    /   \     |   \/   | |   ____|
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`|  | |   \|  | |  |  __     |  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ | |  |  |  | |   __|     \   \        \   \    |  | |  . `  | |  | |_ |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| | |  `--'  | |  |____.----)   |   .----)   |   |  | |  |\   | |  |__| |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______|  \______/  |_______|_______/    |_______/    |__| |__| \__|  \______|     \______| /__/     \__\ |__|  |__| |_______|
"""

def user_guess():
    global NUMBER
    guess = int(input("Enter your guess :"))
    if guess == NUMBER:
        print("You have guessed correct!")
        return True
    diff = guess - NUMBER 
    if diff>0:
        if diff>10:
            print("too high")
        else:
            print("high")
    else:
        if diff>-10:
            print("low")
        else:
            print("too low")
    print("______________________________________________")
    return False


def difficulty():
    choice = input("Do you want to play 'easy' or 'hard'? :").lower()
    if choice == 'hard':
        guess_no =5
    else:
        guess_no = 10
    return guess_no


os.system("cls")
print(logo)
guess_no = difficulty()
print("Welcome to the guessing game")
print("The number has been chosen. The Game begins!")

while not game_end and guess_no>0:
    print(f"{guess_no} guess left")
    game_end =user_guess()
    guess_no -= 1
print("Game Over.")
