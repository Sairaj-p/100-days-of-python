# Virtual coffee machine

#Raw materials
MENU = {
    "espresso": {
        "ingredients": {
            "milk":0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit =0
conti = True
coins =[0,0,0,0]
ingredients ={
"milk" : 200,
"coffee" : 100,
"water" : 300,
}

#functions divided by work

def check_material(order):
    global ingredients,MENU
    order_ingredients = MENU[order]["ingredients"]
    for orders in MENU:
        if order == orders:
            if ingredients['milk'] < order_ingredients['milk']:
                return False
            elif ingredients['water'] < order_ingredients['water']:
                return False
            elif ingredients['coffee'] < order_ingredients['coffee']:
                return False
            else:
                return True


def print_report():
    global ingredients
    print(f"Milk: {ingredients['milk']}ml")
    print(f"Water: {ingredients['water']}ml")
    print(f"Coffee: {ingredients['coffee']}gm")


def coin_collecting():
    coins[0] = int(input("Quaters:"))
    coins[1] = int(input("Dimes:"))
    coins[2] = int(input("Nickels:"))
    coins[3] = int(input("Pennies:"))
    money = coins[0]*0.25 + coins[1]*0.1 + coins[2]*0.5 +coins[3]*0.1
    return(money)


def order(order,money):
    global MENU,ingredients,profit
    for orders in MENU:
        if orders == order:
                if money> MENU[order]["cost"]:
                    ingredients = final_order(order)
                    print(f"your change :{round(money - MENU[order]['cost'],2)}")
                    profit+= MENU[order]['cost'] 
                    print(f"\nHere id s your {order}")
                    return ingredients
                else:
                    print("You have not given enought money to the machine")   
                    return ingredients 
    

def final_order(order):
    global MENU,ingredients
    order_ingredients =MENU[order]["ingredients"]
    ingredients["water"] -= order_ingredients["water"] 
    ingredients["milk"] -= order_ingredients["milk"] 
    ingredients["coffee"] -= order_ingredients["coffee"] 
    # print(f"test :{ingredients}")
    return ingredients


# main brain

while conti:
    print_report()
    choice = input("espresso/cappuccino/latte :")
    conti = check_material(choice)
    if conti:
        money = coin_collecting()
        ingredients = order(choice,money)
    else:
        print("\n\nMachine is out of stock of materials please come back later!\n\n")
print(f"Machine Profit ${profit}")

    