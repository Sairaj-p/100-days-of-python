#Calculator
import os
#Material
operation ={
    "+":addition,
    "-":subtraction,
    "*":multiply,
    "/":division
}
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#machine
def addition(a):
     b = float(input("Second no:"))
     print( a ,'+', b )
     return  a+b 

def subtraction(a):
    b = float(input("Second no:"))
    print(a ,'-', b)
    if(a>b):
        return a-b
    else:
        return b-a

def multiply(a):
    b= float(input("Second no:"))
    print(a ,'*',b)
    return a * b

def division(a):
     b =float(input("Divisor:"))
     print(a ,'/',b)
     return a / b

#Main Body
os.system("cls")
print(logo)
while True:
    a = float(input("First no:"))
    cont = True
    while cont:
        function = input("Operator:")
        result = operation[function](a)
        print("= ",result)
        choice =input("Do you want to continue with same result 'y'or'no':").lower()
        if choice == 'y':
            a = result
            cont = True
        else:
            cont = False

        