#Pong Game

from turtle import Turtle,Screen
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

class Paddle(Turtle):

    def __init__(self,xcor):
        super().__init__()
        self.shape ("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(xcor,0)
         
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-20)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+20)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.move_speed = 0.1

    def move(self):
        self.forward(10)
        if self.ycor() > 280 or self.ycor() <-280:
            self.bounce()
        
    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1

    def bounce(self):
        self.setheading(360-self.heading())

    def paddle_bounce(self):
        self.setheading(180-self.heading())
        self.move_speed *= 0.9

class Score(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(xcor,250)
        self.score = 0
        self.write(self.score,align ="center",font=("Courier",20,"normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score,align ="center",font=("Courier",20,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align ="center",font=("Courier",80,"normal"))
        


paddle_1 = Paddle(380)
paddle_2 = Paddle(-390)
ball = Ball()
game_on = True
score_1 = Score(-100)
score_2 = Score(100)
while game_on:
    screen.update()
    sleep(ball.move_speed)
    screen.listen()
    screen.onkey(paddle_1.move_up,"Up")
    screen.onkey(paddle_1.move_down,"Down")
    screen.onkey(paddle_2.move_up,"w")
    screen.onkey(paddle_2.move_down,"s")
    ball.move()
    if ball.distance(paddle_1)<50 and ball.xcor()>=360 or ball.distance(paddle_2)<50 and ball.xcor()<=-370:
        ball.paddle_bounce()
    if ball.xcor() < -400 :
        ball.reset()
        score_2.update_score()
    if  ball.xcor()>400:
        ball.reset()
        score_1.update_score()
    if score_1.score > 4 or score_2.score>4:
        score_1.game_over()
        game_on = False

screen.exitonclick()