#higher Lower Game
import os
import Day_14_Data
from Day_14_Data import data
from random import randint

start = randint(0,10)
game_on = True
score =-1
def check(start,skip,choice):
    if choice == 'a'and data[start]['follower_count']>data[start+skip]['follower_count']:
        print("Correct.")
        return True
    elif choice == 'b' and data[start]['follower_count']<data[start+skip]['follower_count']:
        print("Correct.")
        return True
    else:
        return False 

   
while game_on:
    os.system("cls")
    print(Day_14_Data.logo)
    skip = randint(1,3)
    score += 1
    print(f"your score is :{score}")
    print(f"\n{data[start]['name']} is a {data[start]['description']} from {data[start]['country']}\n")
    print(Day_14_Data.vs)
    start += skip
    print(f"\n{data[start]['name']} is a {data[start]['description']} from {data[start]['country']}\n")
    choice = input("Who has more followers'a' or 'b' :").lower()
    game_on = check(start-skip,skip,choice)
print("\nyour choice is wrong!")
print(f"\nGame over your score is {score}")

