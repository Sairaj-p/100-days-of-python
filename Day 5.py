#strong password generater

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_letters= int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input(f"How many symbols would you like?\n"))
no_numbers = int(input(f"How many numbers would you like?\n"))

total = no_letters+no_numbers+no_symbols
password = ""
letter = random.randint(0,len(letters)-1)
password += letters[letter]
letter_count =1
number_count =0
symbol_count = 0

for no in range(1,total):
    not_selected = True
    while not_selected:
        choice= random.randint(0,3)
        if choice == 0:
            if(letter_count<no_letters):
                password += letters[random.randint(0,len(letters)-1)]
                letter_count += 1
                not_selected = False
            else:
                 not_selected = True
        elif choice ==1:
            if(number_count<no_numbers):
                password += numbers[random.randint(0,len(numbers)-1)]
                number_count += 1
                not_selected = False
                
            else:
                not_selected = True
        else:
            if(symbol_count<no_symbols):
                password += symbols[random.randint(0,len(symbols)-1)]
                symbol_count += 1
                not_selected = False
            else:
                not_selected = True

print(f"Your strong password is: {password}")




    
