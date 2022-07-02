#choose your adventure treasure hunt

print("Welcome to the treasure hunt \nYour mission is to find the treasure")
crossroad = input("You are at a crossroad would you like to go to 'right' or 'left':").lower()
if crossroad == "left":
    lake = input("You are at a lake, would you like to 'swim' or 'wait' for a boat:").lower()
    if lake == "wait":
        door = input("you have arrived at an island with a house \nthe house has 3 door'red', 'yellow' and 'blue' \nwhich door would you choose:").lower()
        if door == "yellow":
            print("You found the Treasure, You won!")
        elif door =="red":
            print("Burned by fire, Game Over")
        elif door =="blue":
            print("Eaten by Beast, Game Over")
        else:
            print("Game Over")
    else:
        print("Attackd by trouts, Game Over")

else:
    print("You have fallen into a hole, Game Over")

