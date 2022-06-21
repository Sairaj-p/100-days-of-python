#Snake Game with OOP

from turtle import Turtle,Screen
from time import sleep
from random import randint

#setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width =600,height=600)
screen.title("Snake Game")
screen.tracer(0)
exit = False

#Snake creation and funtionalities
class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(0,3):
            s = Turtle(shape ="square")
            s.color("white")
            s.penup()
            s.goto(x=-i*10,y=0)
            self.snake_body.append(s)
        self.head = self.snake_body[0]

    def add_segment(self):
        s = Turtle(shape ="square")
        s.color("white")
        s.penup()
        s.goto(x=self.snake_body[len(self.snake_body)-1].xcor(),y=self.snake_body[len(self.snake_body)-1].ycor())
        self.snake_body.append(s)

    def check_pos(self):
        if self.head.xcor() > 290:
            self.head.goto(-290,self.head.ycor())
        elif self.head.xcor() < -290:
            self.head.goto(290,self.head.ycor())
        elif self.head.ycor() > 290:
            self.head.goto(self.head.xcor(),-290)
        elif self.head.ycor() < -280:
            self.head.goto(self.head.xcor(),290)

    def forward(self):
        for i in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x,new_y)
        self.head.forward(20)
        snake.check_pos()

    def check(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) <10:
                score.game_over()
                return True
               
        return False
           
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

#Food generation and relocation
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(0.5)
        self.goto(40*randint(-7,7),40*randint(-7,7))

    def refresh(self):
        self.goto(40*randint(-7,7),40*randint(-7,7))

#Score_Board
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,280)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score} ",align ="center",font=("Courier",10,"normal"))
        
    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ",align ="center",font=("Courier",10,"normal"))

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game Over",align ="center",font=("Courier",50,"normal"))


#Main Brain
snake = Snake()
food = Food()
score = Score()
screen.update()
while not exit:
    screen.update()
    sleep(0.1)
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.add_segment()
        score.refresh()
    screen.listen()
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    snake.forward()
    exit = snake.check()
    
screen.exitonclick()