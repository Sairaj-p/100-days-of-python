#Multi color Art Maker GUI

import random
import turtle as t
tin = t.Turtle()
tin.hideturtle()
screen =t.Screen()
tin.speed(0)
t.colormode(255)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19),
(133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
(105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
(107, 127, 153), (174, 94, 97), (176, 192, 209)]
tin.pensize(15)
tin.penup()
tin.goto(-450,-370)

def color():
    color = random.choice(color_list)
    return color

def draw():
    tin.pencolor(color())
    tin.pendown()
    tin.forward(1)
    tin.penup()
    tin.forward(30)


def right_side_turn():
    tin.left(90)
    tin.forward(30)
    tin.left(90)
    tin.forward(30)


def left_side_turn():
    tin.right(90)
    tin.forward(30)
    tin.right(90)
    tin.forward(30)

#Main Brain 
if_right_side = True   
for __ in range(0,26):
    for _ in range(0,30):
        draw()
    if if_right_side:
        right_side_turn()
        if_right_side = False
    else :
        left_side_turn()
        if_right_side = True
    
screen.exitonclick()
