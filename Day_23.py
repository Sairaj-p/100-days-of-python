#Car crossing Game

from random import choice,randint
from turtle import Turtle,Screen
import time

colors = ["red", "orange","yellow","green","blue","Purple"]
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
count =0
cars = []
speed = 0.2


class User(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.goto(0,-280)

    def move(self):
        self.forward(10)
    def reset(self):
        self.goto(0,-280)

class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-225,275)
        self.level = 1
        self.write(f"Level = {self.level}",align ="center",font=("Courier",15,"bold"))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {self.level}",align ="center",font=("Courier",15,"bold"))
 
    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game Over",align ="center",font=("Courier",40,"bold"))

class Car(Turtle):
    def __init__(self,ypos):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2,0)
        self.color(choice(colors))
        self.penup()
        self.setheading(180)
        self.goto(300,ypos)
        
    def move(self):
        self.forward(10)

score = Write()
user = User()
Game_on = True
level_up = True
while Game_on:
    while level_up:
        for i in range(0,50):
            if choice([True,False,False,False,False,False]):
                new_car = Car(randint(-250,250))
                cars.append(new_car)
                count += 1
            for car in cars:
                car.move()
        level_up = False
    screen.update()
    time.sleep(speed)
    screen.listen()
    screen.onkey(user.move,"space")
    if choice([True,False,False,False,False,False]):
        new_car = Car(randint(-250,250))
        cars.append(new_car)
        count += 1
    for car in cars:
        car.move()
        if( user.distance(car)<=20):
            score.game_over()
            Game_on = False
    
    if user.ycor() > 280:
        score.level_up()
        user.reset()
        speed *= 0.5
        level_up = True
    
screen.exitonclick()

