#Silent Auction 

import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bides ={}

def new_bid():
    name = input("Enter your name :")
    bid = int(input("Enter your bid :"))
    bides[name] = bid

def winner():
    os.system("cls")
    highest_bid =0
    winner_name = ""
    for name in bides:
        if bides[name]>highest_bid:
            highest_bid = bides[name]
            winner_name = name
    print(f" the winner is {winner_name} with the bid of ${highest_bid}")

#main code
os.system("cls")
repeat = True
while repeat:
    print(logo)
    print("Welcome to the Auction")
    new_bid()
    ans = input("Are their any more bidders 'y' or 'n' :")
    if ans == 'y':
        repeat = True
        os.system("cls")
    else:
        repeat = False
winner()