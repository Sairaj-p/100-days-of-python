from turtle import Turtle,Screen
from random import choice

#Raw Data
race_on = False
winner =""
screen = Screen()
screen.setup(500,400)
colors = ["red","orange","yellow","green","blue","purple"]
turtles =[]
y_s = [-100,-60,-20,20,60,100]

#Main Brain
user_bet =screen.textinput("Make your Bet","Which turtle will win the bet:")
if user_bet in colors:
    race_on = True
if not race_on:
    screen.exitonclick()
    print("Invalid Input")
else:
    for i in range(0,6):
        t = Turtle(shape = "turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x = -230, y = y_s[i])
        turtles.append(t)

    while race_on:
        for i in range(0,6):
            t = turtles[i]
            t.forward(choice([0,5,10,15]))
            if t.xcor()>230:
                race_on = False
                winner =t.pencolor()

    if winner == user_bet:
        print("You won")
    else:
        print(f"you have lost by {winner}")
            
    screen.exitonclick()