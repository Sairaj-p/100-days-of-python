#Blackjack Game
import os
import random

#Materials
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
start_msg = """
New Game Starts 
"""
card_heart = [1,2,3,4,5,6,7,8,9,10,10,10,10]
card_spade = [1,2,3,4,5,6,7,8,9,10,10,10,10]
card_clubs= [1,2,3,4,5,6,7,8,9,10,10,10,10]
card_diamond=[1,2,3,4,5,6,7,8,9,10,10,10,10]
deck =[card_heart,card_diamond,card_clubs,card_spade]
user_cards = []
dealer_cards =[]


def choiceofcards():
    #Choose the cards for both user and computer
    user_card1 = deck[random.randint(0,3)][random.randint(0,12)]
    user_card2 = deck[random.randint(0,3)][random.randint(0,12)]
    user_cards.append(user_card1)
    user_cards.append(user_card2)
    print(f"Your cards are {user_cards}")
    if 1 in user_cards:
        choice = input("do you want to trun your ace into 11 point? 'y' or 'n'")
        if choice == 'y':
            for index in range(2):
                if user_cards[index] == 1:
                    user_cards[index] = 11
        print(user_cards)
    dealer_card1 = deck[random.randint(0,3)][random.randint(0,12)]
    if(dealer_card1 == 1):
        dealer_card1 = 11
    print(f"computer card is {dealer_card1}")
    choice = input("Do you want to draw one more card? 'y' or 'n'").lower()
    if choice == 'y':
        user_card3 = deck[random.randint(0,3)][random.randint(0,12)]
        user_cards.append(user_card3)
    dealer_card2 = deck[random.randint(0,3)][random.randint(0,12)]
    if(dealer_card1 == 1):
        dealer_card1 = 11
    dealer_cards = [dealer_card1,dealer_card2]
    if dealer_card1+dealer_card2<17:
        dealer_card3 = deck[random.randint(0,3)][random.randint(0,12)]
        dealer_cards.append(dealer_card3)
       # cards = []
    return user_cards ,dealer_cards
    
def winner(user_cards,dealer_cards,amount):
    #Check all conditions to find a winner
    if sum(user_cards)>21:
        print("Dealer wins!")
        return amount-100
    if 11 in dealer_cards and  sum(dealer_cards)>21:
        dealer_cards.remove(11)
        dealer_cards.append(1)
    if sum(user_cards)>sum(dealer_cards) or sum(dealer_cards)>21:
        print("You win!")
        return amount+100
    elif sum(user_cards)<sum(dealer_cards):
        print("Dealer wins!")
        return amount-100
    else:
        print("Draw")
        return amount


#Main Brain
amount = 200
os.system("cls")
print(logo)
print("Welcome to the table!")
while amount>=100:
    print(start_msg)
    user_cards = []
    dealer_cards = []
    user_cards,dealer_cards =choiceofcards()
    print(f"Yours final hand is {user_cards}")
    print(f"Dealer final hand is {dealer_cards}")
    amount =winner(user_cards,dealer_cards,amount)
    print(f"You have {amount}")



