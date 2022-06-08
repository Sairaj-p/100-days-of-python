#Ceasar Cipher
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 

           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
def encode(msg,shift):
    print("encode")
    cipher =""
    msg = list(msg)
    for i in range(len(msg)):
        for j in range(26):
            if msg [i] == alphabet[j]:
                cipher += alphabet[j+shift]
    print(f" your message is :{cipher}")


def decode(msg,shift):
    print("decode")
    cipher =""
    msg = list(msg)
    for i in range(len(msg)):
        for j in range(26,len(alphabet)):
            if msg [i] == alphabet[j]:
                cipher += alphabet[j-shift]
    print(f" your message is :{cipher}")


os.system("cls")
print(logo)
repeat = True
while repeat:
    direction = input("do you want to 'encode' or 'decode' ").lower()
    msg = input("Enter your message:").lower()
    shift = int(input("Enter the shift :"))-1
    if (direction == 'encode'):
        encode(msg,shift)
    elif direction == 'decode':
        decode(msg,shift)
    ans =input("Do you want to continue 'y' or 'n':").lower()
    if(ans == 'y'):
        repeat = True
    else:
        repeat = False
